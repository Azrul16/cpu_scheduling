import threading, time, random
from queue import Queue

# Bounded buffer
buffer_size = 5
buffer = Queue(maxsize=buffer_size)

def producer(pid):
    while True:
        item = random.randint(100, 999)
        buffer.put(item)  # Waits if buffer is full
        print(f"Producer-{pid} produced: {item}")
        time.sleep(random.uniform(0.5, 1.5))

def consumer(cid):
    while True:
        item = buffer.get()  # Waits if buffer is empty
        print(f"Consumer-{cid} consumed: {item}")
        time.sleep(random.uniform(1, 2))

# Start multiple producers and consumers
for i in range(2):
    threading.Thread(target=producer, args=(i,), daemon=True).start()

for i in range(2):
    threading.Thread(target=consumer, args=(i,), daemon=True).start()

# Run the simulation for a limited time
time.sleep(10)
