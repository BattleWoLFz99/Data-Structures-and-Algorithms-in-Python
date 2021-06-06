# Using List
class MyQueue(object):

    def __init__(self):
        self.MAXSIZE = 4
        self.queue = [0] * self.MAXSIZE
        self.head, self.tail = 0, 0

    def enqueue(self, item):
        queue = self.queue 

        if self.tail == self.MAXSIZE:
            return 

        queue[self.tail] = item 
        self.tail += 1 

    def dequeue(self):
        queue = self.queue

        if self.head == self.tail:
            return -1 

        item = queue[self.head]
        self.head += 1 
        return item 

class Node():
    def __init__(self, _val):
        self.next = None
        self.val = _val
# However, [^, ^, 3, 4], head = 2, tail = 4, so:

# Using DLList
class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.head, self.tail = None, None

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    # @return an integer
    def dequeue(self):
        if self.head is not None:
            item = self.head.val
            self.head = self.head.next
            return item
        return -1