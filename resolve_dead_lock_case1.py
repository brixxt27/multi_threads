import threading
import time

resource_1 = threading.Lock()
resource_2 = threading.Lock()

def thread_A_task():
    print("[A] 자원 1 획득 시도")
    resource_1.acquire()
    print("[A] 자원 1 획득 완료")
    time.sleep(0.1)
    print("[A] 자원 2 획득 시도")
    resource_2.acquire()
    print("[A] 모든 자원 획득 완료")
    resource_2.release()
    resource_1.release()

def thread_B_task():
    print("[B] 자원 1 획득 시도")
    resource_1.acquire()
    print("[B] 자원 1 획득 완료")
    time.sleep(0.1)
    print("[B] 자원 2 획득 시도")
    resource_2.acquire()
    print("[B] 모든 자원 획득 완료")
    resource_2.release()
    resource_1.release()

t1 = threading.Thread(target=thread_A_task)
t2 = threading.Thread(target=thread_B_task)
t1.start()
t2.start()
t1.join()
t2.join()
print("작업 종료")