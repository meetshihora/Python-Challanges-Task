# Task 2: print total active threads in multithreaded code using threading.active_count()

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

    print(f"Active threads count: {threading.active_count()}")

for th in threads:
    th.join()

print("All threads have finished.")
print(f"Final active threads count: {threading.active_count()}")
