class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0

        # state: dp[i][j] = min_sum from (0, 0) tp (i, j)
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * m for _ in range(n)]

        # init:
        dp[0][0] = grid[0][0] 
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # func:
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        # ans
        return dp[n - 1][m - 1]


# 滚动数组优化
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0

        # state: dp[i][j] = min_sum from (0, 0) tp (i, j)
        # RA：改滚动数组数字代表步骤
        # RA1：一般func最外层参数改掉成数字that从func里推导都没错
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * m for _ in range(2)]

        # init: RA2：只扔要磨的，不能无脑都扔 func 里。万一就一行 func 进不去就不能 init
        dp[0][0] = grid[0][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # func: RA3：只磨dp里的参数，不要无脑看到 i 就磨有时候 i 会指代 j 就不能磨
        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + grid[i][0]
            for j in range(1, m):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - 1]) + grid[i][j]
        
        # ans
        return dp[(n - 1) % 2][m - 1]