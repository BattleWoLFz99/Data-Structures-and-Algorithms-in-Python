class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if not A:
            return 

        n = len(A)

        # state
        dp = [False] * n

        # init
        dp[0] = True

        # function
        for i in range(n):
            for j in range(i):
                dp[i] = dp[i] or dp[j] and (j + A[j] >= i)

        return dp[n - 1]