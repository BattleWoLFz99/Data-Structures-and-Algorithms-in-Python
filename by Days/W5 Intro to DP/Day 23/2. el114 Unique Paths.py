# Top-down:

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # state: dp[i][j] 代表从 0, 0 走到 i, j 额方案总数
        # [0] * 3 = [0, 0, 0]
        dp = [[0] * n for _ in range(m)]
        # DO NOT dp=[[0] * n] * m, it does not generate new array
        # for instance, dp = [[0, 0], [0, 0]]
        # dp[0][0] = 1
        # => dp = [[1, 0], [1, 0]]

        # initialize: 初始化第0行和第0列
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # function: dp[i][j] = dp[i - 1] + dp[i][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # answer
        return dp[m - 1][n - 1]


# Bottom-up

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # state: dp[i][j] 代表从 0, 0 走到 i, j 额方案总数
        dp = [[0] * n for _ in range(m)]

        # initialize: 初始化第 m - 1 行和第 n - 1 列
        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1

        # function: dp[i][j] = dp[i + 1] + dp[i][j + 1]
        for i in range(m - 2, -1, -1):
            for j in range(n -2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        # answer
        return dp[0][0]