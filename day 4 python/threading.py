import threading

def task():
    print("Thread is running")
    t = threading.Thread(target=task)
    t.start()
    t.join()

print("Main thread ends")

import threading

def task():
    print("Thread is running")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task, args=("Thread2",))
t1.start()
t2.start()
t1.join()
t2.join()

print("Main thread ends")