# Recursion Ver, TLE
# 还挺难理解进去的，但是不能只看AC不然基础功不扎实。但一定不是入门的

class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def canWinBash(self, n):
        if n <= 3:
            return True

        return not self.canWinBash(n - 1) or \
               not self.canWinBash(n - 2) or \
               not self.canWinBash(n - 3)


# AC:
    def canWinBash(self, n):
        return n % 4 != 0