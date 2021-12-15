# list 改动才是直接改，数值相加记得前面初始化 return 后面 return
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n == 0:
            return 0

        return self.dfs(n, {})

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0

        result = 0
        for i in range(1, 3):
            n -= i
            result += self.dfs(n, memo)
            n += i
        memo[n] = result
        return memo[n]