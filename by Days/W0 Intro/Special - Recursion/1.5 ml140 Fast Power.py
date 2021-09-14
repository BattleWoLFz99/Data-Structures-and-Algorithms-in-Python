# O(n), TLE

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b

        # a^n % b = (a % b) * (a^(n - 1) % b) % b
        #         = (a % b) * (     y    % b) % b
        x = a % b
        y = self.fastPower(a, b, n - 1)

        return x * y % b

# // 2 去 Day 31