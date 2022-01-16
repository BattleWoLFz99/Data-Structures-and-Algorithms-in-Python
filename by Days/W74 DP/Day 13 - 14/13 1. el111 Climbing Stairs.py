class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        # dp[i] = steps to i
        dp = [0] * (n + 1)
        
        # init:
        dp[0] = 1
        dp[1] = 1
        
        # func: dp[i] = dp[i - 1] + dp[i - 2]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        # ans
        return dp[n]


# Rolling Array:
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        # dp[i] = steps to i
        dp = [0] * 3
        
        # init:
        dp[0] = 1
        dp[1] = 1
        
        # func: dp[i] = dp[i - 1] + dp[i - 2]
        for i in range(2, n + 1):
            dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3]
            
        # ans
        return dp[n % 3]