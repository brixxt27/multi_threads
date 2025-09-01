import threading
import time

visitors_count = 0

def count_visitors():
    global visitors_count
    for _ in range(100000):
        temp = visitors_count
        time.sleep(0.000001)
        temp += 1
        visitors_count = temp

thread1 = threading.Thread(target=count_visitors)
thread2 = threading.Thread(target=count_visitors)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("기대하는 방문자 수:   200000")
print("실제 방문자 수:      ", visitors_count)

# 출력값
# 기대하는 방문자 수:   200000
# 실제 방문자 수:       100001
