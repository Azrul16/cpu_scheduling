import threading, time
import random

n = 5
forks = [threading.Lock() for _ in range(n)]

def philosopher(i):
    while True:
        print(f"Philosopher {i} is thinking.")
        time.sleep(random.random())
        print(f"Philosopher {i} is hungry.")
        left = forks[i]
        right = forks[(i + 1) % n]
        with left:
            with right:
                print(f"Philosopher {i} is eating.")
                time.sleep(random.random())

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(n)]
for t in threads: t.start()
