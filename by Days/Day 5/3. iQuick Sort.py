# This version of quick sort does not use any extra space because it sorts the list in-place.

# quick sort
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
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
        # Line 23 - 33: Partition
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        
        # then, %left% is on the right side, %right% is on the keft side.
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


s = Solution()
A = [1, 23, 5, 63, 324, 5, 6, 1]
s.sortIntegers(A)
print(A)