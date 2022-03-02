# V1 TLE (DP needed)
# Intro to Stars and Bars

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        n, max_profit = len(prices), 0
        for i in range(n):
            left_profit = self.get_profit(prices, 0, i)
            right_profit = self.get_profit(prices, i, n)
            max_profit = max(max_profit, left_profit + right_profit)

        return max_profit

    def get_profit(self, prices, start, end):
        min_price, profit = float('inf'), 0
        for i in range(start, end):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)
        return profit