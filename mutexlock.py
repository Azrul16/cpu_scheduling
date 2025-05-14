import threading

lock = threading.Lock()

def critical_section(thread_id):
    for _ in range(3):
        lock.acquire()
        print(f"Thread {thread_id} entering critical section.")
        time.sleep(1)
        print(f"Thread {thread_id} exiting critical section.")
        lock.release()
        time.sleep(1)

threads = [threading.Thread(target=critical_section, args=(i,)) for i in range(2)]
for t in threads: t.start()
for t in threads: t.join()
