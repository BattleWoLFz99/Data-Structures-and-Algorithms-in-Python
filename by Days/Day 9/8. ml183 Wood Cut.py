class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0

        start, end = 1, min(max(L), sum(L) // k)

        if end < 1:
            return 0

        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_count(L, mid) > k:
                start = mid
            elif self.get_count(L, mid) == k:
                start = mid
            else:
                end = mid
        
        return end if self.get_count(L, end) >= k else start

    def get_count(self, L, length):
        return sum(l // length for l in L)