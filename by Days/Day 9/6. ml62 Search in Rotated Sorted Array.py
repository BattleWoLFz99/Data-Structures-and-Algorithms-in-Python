class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        index = self.find_min_index(A)
        if A[index] <= target <= A[-1]:
            return self.binary_search(A, index, len(A) - 1, target)
        return self.binary_search(A, 0, index - 1, target)

    def find_min_index(self,A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[end]:
                end = mid
            else:
                start = mid

        if A[start] < A[end]:
            return start
        return end

    def binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1


# One Partition:
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[end]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
        
        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1
        