from queue import Queue
q = Queue()
count = 1000

while count > 0:
    q.dequeue()
    print(count)