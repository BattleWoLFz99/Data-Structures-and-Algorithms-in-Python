# It is bad:

class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.MAXSIZE = 4
        self.queue = [0] * self.MAXSIZE
        self.head, self.tail = 0, 0

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        queue = self.queue 

        # 队列满 
        if self.tail == self.MAXSIZE:
            return 

        queue[self.tail] = item 
        self.tail += 1 


    # @return an integer
    def dequeue(self):
        queue = self.queue 

        ## 队列为空
        if self.head == self.tail:
            return -1 

        item = queue[self.head]
        self.head += 1 
        return item 

# Space wasted if:
#   enqueue(1)
#   enqueue(2)
#   enqueue(3)
#   enqueue(4)
#   dequeue()
#   dequeue()

# Go check el492, then Circular Queue:

class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.SIZE = 100000
        self.queue = [0] * self.SIZE
        self.head, self.tail = 0, 0

    # @param {int} item an integer
    # @return nothing
    # 压入队列
    def enqueue(self, item):
        queue = self.queue 

        # 队列满 
        if (self.tail + 1) % self.SIZE == self.head:
            return 

        queue[self.tail] = item 
        self.tail = (self.tail + 1) % self.SIZE


    # @return an integer
    # 弹出元素
    def dequeue(self):
        queue = self.queue 

        ## 队列为空
        if self.head == self.tail:
            return -1 

        item = queue[self.head]
        self.head = (self.head + 1) % self.SIZE
        return item 