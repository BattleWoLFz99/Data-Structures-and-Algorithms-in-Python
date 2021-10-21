class Solution:
    def sortIntegers(self, A):
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        if start >= end:   # Only 1 num
            return

        left, right = start, end
        # key point 1: pivot is the value, not the index
        # Don't A[start] or A[end], in case the array is already sorted. 
        pivot = A[(start + end) // 2]

        # key point 2: every time you compare left & right, it should be
        # left <= right not left < right
        # Partition:
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


s = Solution()
A = [1, 3, 4, 2, 1, 3, 4]
s.sortIntegers(A)
print(A)