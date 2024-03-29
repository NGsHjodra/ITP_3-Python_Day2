import threading

# create two resources
resource1 = threading.Lock()
resource2 = threading.Lock()

# # define a function that uses both resources
# def foo():
#     with resource1:
#         print("Acquired resource 1")
#         with resource2:
#             print("Acquired resource 2")

# # define another function that uses the resources in the opposite order
# def bar():
#     with resource2:
#         print("Acquired resource 2")
#         with resource1:
#             print("Acquired resource 1")

# define a function that uses both resources
def foo():
    resource1.acquire()
    print("Acquired resource 1")
    resource2.acquire()
    print("Acquired resource 2")
    resource2.release()
    resource1.release()

# define another function that uses the resources in the opposite order
def bar():
    resource2.acquire()
    print("Acquired resource 2")
    resource1.acquire()
    print("Acquired resource 1")
    resource1.release()
    resource2.release()

# create two threads, each calling a function that uses the resources in a different order
thread1 = threading.Thread(target=foo)
thread2 = threading.Thread(target=bar)

# start both threads
thread1.start()
thread2.start()

# wait for both threads to finish
thread1.join()
thread2.join()