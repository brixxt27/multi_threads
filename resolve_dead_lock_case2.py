import threading
import time

resource_1 = threading.Lock()
resource_2 = threading.Lock()
success_lock = threading.Lock()
successful_runs = 0

def thread_A_task():
    global successful_runs
    while True:        
        print("[A] 자원 1 획득 시도")
        resource_1.acquire()
        print("[A] 자원 1 획득 완료")

        print("[A] 자원 2 획득 시도 (1초 대기)")
        acquired_r2 = resource_2.acquire(timeout=1)
        
        if not acquired_r2:
            print("🚨 [A] 자원 2 획득 실패. 점유했던 자원 1을 포기합니다.")
            resource_1.release()
            time.sleep(0.5)
            continue
        
        print("✅ [A] 모든 자원 획득 완료. 작업 수행...")
        time.sleep(0.2)
        
        with success_lock:
            successful_runs += 1
            
        resource_2.release()
        resource_1.release()
        print("[A] 작업 완료 후 모든 자원 반납")
        break

def thread_B_task():
    global successful_runs
    while True:
        print("[B] 자원 2 획득 시도")
        resource_2.acquire()
        print("[B] 자원 2 획득 완료")
        
        print("[B] 자원 1 획득 시도 (1초 대기)")
        acquired_r1 = resource_1.acquire(timeout=1)
        
        if not acquired_r1:
            print("🚨 [B] 자원 1 획득 실패. 점유했던 자원 2를 포기합니다.")
            resource_2.release()
            time.sleep(0.5)
            continue
            
        print("✅ [B] 모든 자원 획득 완료. 작업 수행...")
        time.sleep(0.2)
        
        with success_lock:
            successful_runs += 1

        resource_1.release()
        resource_2.release()
        print("[B] 작업 완료 후 모든 자원 반납")
        break

t1 = threading.Thread(target=thread_A_task)
t2 = threading.Thread(target=thread_B_task)
t1.start()
t2.start()
t1.join()
t2.join()
print("\n모든 작업이 데드락 없이 성공적으로 종료되었습니다.")