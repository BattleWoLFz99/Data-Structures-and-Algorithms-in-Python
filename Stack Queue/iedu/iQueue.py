class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size

if __name__ == "__main__" :
    queue_obj = MyQueue()
    print("is_empty(): " + str(queue_obj.is_empty()))
    print("front(): " + str(queue_obj.front()))
    print("rear(): " + str(queue_obj.rear()))
    print("size(): " + str(queue_obj.size()))


class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size
    
    def enqueue(self, value):
        self.queue_size += 1
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front

if __name__ == "__main__" :
    queue_obj = MyQueue()
    print("queue.enqueue(2);")
    queue_obj.enqueue(2)
    print("queue.enqueue(4);")
    queue_obj.enqueue(4)
    print("queue.enqueue(6);")
    queue_obj.enqueue(6)
    print("queue.enqueue(8);")
    queue_obj.enqueue(8)
    print("queue.enqueue(10);")
    queue_obj.enqueue(10)
    print("is_empty(): " + str(queue_obj.is_empty()))
    print("front(): " + str(queue_obj.front()))
    print("rear(): " + str(queue_obj.rear()))
    print("size(): " + str(queue_obj.size()))
    print("Dequeue(): " + str(queue_obj.dequeue()))
    print("Dequeue(): " + str(queue_obj.dequeue()))
    print("front(): " + str(queue_obj.front()))
    print("back(): " + str(queue_obj.rear()))
    print("queue.enqueue(12);")
    queue_obj.enqueue(12)
    print("queue.enqueue(14);")
    queue_obj.enqueue(14)

while queue_obj.is_empty() is False:
    print("Dequeue(): " + str(queue_obj.dequeue()))

print("is_empty(): " + str(queue_obj.is_empty()))
