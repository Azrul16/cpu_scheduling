import threading
import time

flag = [False, False]
turn = 0

def peterson(process_id):
    global flag, turn
    other = 1 - process_id
    for _ in range(5):
        flag[process_id] = True
        turn = other
        while flag[other] and turn == other:
            pass  # wait

        # Critical Section
        print(f"Process {process_id} is in critical section.")
        time.sleep(1)

        # Exit section
        flag[process_id] = False
        time.sleep(1)

t1 = threading.Thread(target=peterson, args=(0,))
t2 = threading.Thread(target=peterson, args=(1,))

t1.start()
t2.start()
t1.join()
t2.join()
