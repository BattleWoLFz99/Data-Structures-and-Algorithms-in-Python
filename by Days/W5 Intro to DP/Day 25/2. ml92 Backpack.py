# However it TLE (or is faster than + )
# Prerep for 3.

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if not A:
            return 0

        n = len(A)
        # state: dp[i][j] 代表前 i 个数里能否挑出 <= j 的最大和
        # init: 都是 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # function
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        # answer
        return dp[n][m]