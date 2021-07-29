class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return -1
        # [[]] out of range

        n = len(triangle)

        # State
        dp = [[0] * n, [0] * n]

        # Init
        dp[0][0] = triangle[0][0]

        # Function
        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]
            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[(i - 1) % 2][j]) \
                + triangle[i][j]

        # Answer
        return min(dp[(n - 1) % 2])