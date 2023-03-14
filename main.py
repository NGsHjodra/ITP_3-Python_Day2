import time
import threading
import requests

def search(qry):
    res = requests.get(f"https://www.google.com/search?q={qry}")
    # print status code
    print(f"Status code: {res.status_code} for {qry}")
    # save to file
    with open(f"results-{qry}.html", "a") as f:
        f.write(res.text)


# make web request
def searchAll(queries):

    # make a thread for each query
    threads = []
    for qry in queries:
        t = threading.Thread(target=search, args=(qry,))
        t.start()
        threads.append(t)

    # wait for all threads to finish
    for t in threads:
        t.join()

queries = ['test', 'rest', 'best', 'west', 'rat', 'bat', 'cat', 'mat']

# measure time
start = time.time()
searchAll(queries)
end = time.time()
diff = end - start
print(f"Time taken: {diff} seconds")