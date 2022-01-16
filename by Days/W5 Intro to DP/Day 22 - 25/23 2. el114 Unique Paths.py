# Top-down
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 

        # state: dp[i][j] = paths from (0, 0) to (i, j)
        dp = [[0] * m for _ in range(n)]

        # init 记得(0, 0)也带1，不然后续滚动数组容易错
        dp[0][0] = 1
        for i in range(1, n):
            dp[i][0] = 1
        for j in range(1, m):
            dp[0][j] = 1

        # func
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # ans
        return dp[n - 1][m - 1]

# 滚动数组优化
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 

        # state: dp[i][j] = paths from (0, 0) to (i, j)
        # RA：滚动数组优化
        # RA2：func 滚最外层参数 state 里改成数字that从func里判断
        dp = [[0] * m for _ in range(2)]

        # RA1：init 扔到 func 里面去。只扔磨的，如果扔j如果只有一行func根本进不去没法init
        dp[0][0] = 1
        for j in range(m):
            dp[0][j] = 1

        # func
        # RA3：一般有且只有dp里的func最外层参数磨RA2里的数字都没错
        # 这么说的意义是不要看到i就磨容易写错。。dp里的i才能磨且有时i会代表j就不能磨
        for i in range(1, n):
            dp[i % 2][0] = 1
            for j in range(1, m):
                dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]

        # ans：RA4：ans记得磨
        return dp[(n - 1) % 2][m - 1]

# Bottom-up
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # state: dp[i][j] 代表从 [i][j] 走到 [m - 1], [n - 1] 的方案总数
        dp = [[0] * n for _ in range(m)]

        # initialize: 初始化第 m - 1 行和第 0 列
        # 这里 m n 二刷还是写反了。。好好看画的图！
        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1

        # function: dp[i][j] = dp[i + 1] + dp[i][j + 1]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        # answer
        return dp[0][0]


