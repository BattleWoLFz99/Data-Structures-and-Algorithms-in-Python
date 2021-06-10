class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        neg_cnt = self.partition(A)
        pos_cnt = len(A) - neg_cnt

        if neg_cnt > pos_cnt:
            left = 1
            right = len(A) - 1
        elif neg_cnt < pos_cnt:
            left = 0
            right = len(A) - 2
        else:
            left = 0
            right = len(A) - 1
            
        return self.interleaving(A, left, right)

    def partition(self, A):
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] < 0:
                left += 1
            while left <= right and A[right] > 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        return left
        
    def interleaving(self, A, left, right):
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2

        return A