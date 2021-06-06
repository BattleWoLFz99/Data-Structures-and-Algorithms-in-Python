class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if len(L) == 0:
            return 0
        start, end, ans = 1, max(L), 0
        while start <= end:
            mid = (start + end) // 2
            if self.check(L, k, mid):
                start, ans = mid + 1, mid
            else:
                end = mid - 1
        return ans

    def check(self, L, k, mid):
        sum = 0
        for i in L:
            sum += i // mid
        if sum < k:
            return False
        else:
            return True