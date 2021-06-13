# Educative.io
class TwoStacks:
    # constructor
    def __init__(self, n):  
        self.size = n
        # populating 0s on all n indices of array arr
        self.arr = [0] * n  
        self.top1 = -1
        self.top2 = self.size

    # Method to push an element x to stack1
    def push1(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to push an element x to stack2
    def push2(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack Underflow ")
            exit()


if __name__ == "__main__" :
    stack = TwoStacks(10)
    stack.push1(20)
    stack.push2(10)
    stack.push2(20)
    stack.push2(30)
    stack.push2(40)
    print(stack.pop1())
    stack.push1(100)
    print(stack.pop2())
    print(stack.arr)


