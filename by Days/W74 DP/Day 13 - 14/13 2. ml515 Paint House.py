class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        if not costs:
            return 0

        # state: 前 i 个房子成功染色，且最后一个房子的颜色为 j
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]

        # init: 
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        # func: dp[i][j] = min(dp[i - 1](other j)) + costs[i][j]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

        return min(dp[n - 1])

# 只磨dp。。一刷习惯性都磨了把 costs 也磨了 debug 老半天
    def minCost(self, costs):
        if not costs:
            return 0

        # state: 前 i 个房子成功染色，且最后一个房子的颜色为 j
        n = len(costs)
        dp = [[0] * 3 for _ in range(2)]

        # init: 
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        # func: dp[i][j] = min(dp[i - 1](other j)) + costs[i][j]
        for i in range(1, n):
            dp[i % 2][0] = min(dp[(i - 1) % 2][1], dp[(i - 1) % 2][2]) + costs[i][0]
            dp[i % 2][1] = min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][2]) + costs[i][1]
            dp[i % 2][2] = min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1]) + costs[i][2]

        # ans: min(dp[n - 1][j])
        return min(dp[(n - 1) % 2])