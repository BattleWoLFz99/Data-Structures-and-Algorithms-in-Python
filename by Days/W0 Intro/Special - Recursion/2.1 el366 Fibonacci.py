# 这里单独加了 memo={} 作为初始化，原来会第一个def初始化后再跟下一个def，应该一样 

class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 2:
            return n - 1

        result = self.fibonacci(n - 1, memo) + self.fibonacci(n - 2, memo)
        memo[n] = result

        return result