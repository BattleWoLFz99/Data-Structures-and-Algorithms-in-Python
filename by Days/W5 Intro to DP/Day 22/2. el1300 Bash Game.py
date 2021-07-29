# V1 stack overflow:

class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def canWinBash(self, n):
        return self.memo_search(n, {})

    def memo_search(self, n, memo):
        if n <= 3:
            return True
        if n in memo:
            return memo[n]

        for i in range(1, 4):
            if not self.memo_search(n - i, memo):
                memo[n] = True
                return True
        memo[n] = False
        return False


# V2

class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def canWinBash(self, n):
        return n % 4 != 0
