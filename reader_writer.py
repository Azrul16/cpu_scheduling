import threading, time

mutex = threading.Lock()
rw_mutex = threading.Lock()
readers = 0

def reader(id):
    global readers
    while True:
        mutex.acquire()
        readers += 1
        if readers == 1:
            rw_mutex.acquire()
        mutex.release()
        
        print(f"Reader {id} is reading")
        time.sleep(1)

        mutex.acquire()
        readers -= 1
        if readers == 0:
            rw_mutex.release()
        mutex.release()
        time.sleep(2)

def writer(id):
    while True:
        rw_mutex.acquire()
        print(f"Writer {id} is writing")
        time.sleep(2)
        rw_mutex.release()
        time.sleep(3)

for i in range(2):
    threading.Thread(target=reader, args=(i,)).start()

for i in range(1):
    threading.Thread(target=writer, args=(i,)).start()
