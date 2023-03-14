import threading
import time

queue = []

lock = threading.Lock()

def produce():
    global queue
    i = 1
    for _ in range(10000):
        try:
            lock.acquire()
            queue.append(i)
            lock.release()    
            # queue.append(i)
            # time.sleep(0.0002)
            # print(f"Produced item {i}")
        except Exception as e:
            print(f"Producer exception: {e.__class__.__name__}: {e}")

def consume():
    global queue
    for _ in range(10000):
        try:
            if queue:
                lock.acquire()
                queue.pop(0)
                lock.release()
                # time.sleep(0.0001)
                # item = queue.pop(0)
                # print(f"Consumed item {item}")
        except Exception as e:
            print(f"Consumer exception: {e.__class__.__name__}: {e}")

for _ in range(100):

    producer_thread = threading.Thread(target=produce)
    producer_thread2 = threading.Thread(target=produce)
    producer_thread3 = threading.Thread(target=produce)

    consumer_thread = threading.Thread(target=consume)
    consumer_thread2 = threading.Thread(target=consume)
    consumer_thread3 = threading.Thread(target=consume)

    producer_thread.start()
    producer_thread2.start()
    producer_thread3.start()

    consumer_thread.start()
    consumer_thread2.start()
    consumer_thread3.start()

    producer_thread.join()
    producer_thread2.join()
    producer_thread3.join()

    consumer_thread.join()
    consumer_thread2.join()
    consumer_thread3.join()