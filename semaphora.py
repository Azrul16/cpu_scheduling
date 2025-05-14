import threading, time, random
from collections import deque

buffer = deque()
buffer_size = 5
empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)
mutex = threading.Lock()

def producer():
    while True:
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Produced: {item}")
        mutex.release()
        full.release()
        time.sleep(random.random())

def consumer():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.popleft()
        print(f"Consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(random.random())

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
