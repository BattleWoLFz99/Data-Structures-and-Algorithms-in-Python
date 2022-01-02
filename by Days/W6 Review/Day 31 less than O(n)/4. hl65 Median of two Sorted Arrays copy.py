# 找 A[k//2] 如果 < B[k//2] 就扔掉 A[k//2] by index_a + k // 2 - 1 一直到 k == 1 返回最小
# 如果超过长度视为无穷大
# 为了 k == 1 直接返回 需要判断是不是刚好
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.find_Kth(A, 0, B, 0, n // 2 + 1)
        return (self.find_Kth(A, 0, B, 0, n // 2) + \
            self.find_Kth(A, 0, B, 0, n // 2 + 1)) / 2

    def find_Kth(self, A, index_a, B, index_b, k):
        if index_a == len(A):
            return B[index_b + k - 1]
        if index_b == len(B):
            return A[index_a + k - 1]
        if k == 1:
            return min(A[index_a], B[index_b])

        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else float('inf')
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else float('inf')

        if a < b:
            return self.find_Kth(A, index_a + k // 2, B, index_b, k - k // 2)
        return self.find_Kth(A, index_a, B, index_b + k // 2, k - k // 2)