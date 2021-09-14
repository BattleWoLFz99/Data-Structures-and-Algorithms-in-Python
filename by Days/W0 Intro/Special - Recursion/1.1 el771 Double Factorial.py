# emm 我也不知道这个 Special 是干嘛的刷了一堆幼儿园题目笑

# 普通版：
class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def doubleFactorial(self, n):
        if n <= 2:
            return n
        
        return n * self.doubleFactorial(n - 2)

# 尾递归
    def doubleFactorial(self, n, result=1):
        if n <= 2:
            return n * result

        return self.doubleFactorial(n - 2, result * n)

# 例如 print_n，打出 6 5 4 3 2 1 
    def print_n(n):
        if n <= 0:
            return

        print(n)
        print_n(n - 1)

    print_n(6)


# 尾递归 改 迭代
    def doubleFactorial(self, n, result=1):
        while True:
            if n <= 2:
                return n * result
            
            next_n, next_result = n - 2, n * result
            n, result = next_n, next_result