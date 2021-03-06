# semaphore_signal.py
#
# An example of using a semaphore to signal

import threading
import time

sema = threading.Semaphore(1)
item = None


def producer():
    global item
    print("I'm the producer and I produce data.")
    print("Producer is going to sleep.")
    item = "Hello"
    time.sleep(2)
    print(item)
    print("Producer is alive. Signaling the consumer.")
    sema.release()


def consumer():
    print("I'm a consumer and I wait for data.")
    print("Consumer is waiting.")
    sema.acquire()
    print("Consumer got", item)
    # sema.release()


t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t3 = threading.Thread(target=consumer)
t4 = threading.Thread(target=consumer)
t1.start()
t2.start()
t3.start()
t4.start()
print('dk;jnbkjdb')