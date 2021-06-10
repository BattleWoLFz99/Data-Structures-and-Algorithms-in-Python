class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        right = self.find_upper_closest(A, target)
        left = right - 1
        
        results = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1

        return results

    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True

        return target - A[left] <= A[right] - target

    def find_upper_closest(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] == target:
                end = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end

        return len(A)
