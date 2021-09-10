import queue

Q = queue.Queue()

Q.put(1)
Q.put(2)
Q.put(3)

while not Q.empty():
    print(Q.get())