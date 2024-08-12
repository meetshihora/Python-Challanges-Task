''' Task 1: Create any multithreaded code using for loop for creating multithreads
        for i in range(10):
            th = Thread(target=func_name, args=(i, ))
'''

import threading
import time

def func_name(thread_number):
    print(f"Thread {thread_number} is starting.")
    time.sleep(1) 
    print(f"Thread {thread_number} is finishing.")


threads = []
for i in range(10):
    th = threading.Thread(target=func_name, args=(i,))
    threads.append(th)
    th.start()

for th in threads:
    th.join()

print("All threads have finished.")
