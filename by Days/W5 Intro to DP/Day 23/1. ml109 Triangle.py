# The bottom-up approach(DP)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if not triangle:
            return []

        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]

        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]

        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j + 1], dp[i + 1][j]) + triangle[i][j]

        return dp[0][0]



# Top-down

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
        dp = [[0] * (i + 1) for i in range(n)]

        # Init
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        # Function
        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        # Answer
        return min(dp[n - 1])


# Top down less code:
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
        dp = [[0] * (i + 1) for i in range(n)]

        # Init
        dp[0][0] = triangle[0][0]

        # Function
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        # Answer
        return min(dp[n - 1])

# Rolling Array: Day 27/1.~