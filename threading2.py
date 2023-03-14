import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    
    for i in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

def run_threads():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

for i in range(100):
    counter = 0
    run_threads()
    if counter != 1000000:
        print(f"{i}: Counter value: {counter}")