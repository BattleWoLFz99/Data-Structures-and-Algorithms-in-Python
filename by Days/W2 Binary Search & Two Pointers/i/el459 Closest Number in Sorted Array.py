class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, results, target):
        if not results:
            return -1

        start, end = 0, len(results) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if results[mid] < target:
                start = mid
            else:
                end = mid
                
        # pay extra attention here:
        if target - results[start] < results[end] - target:
            return start
        else:
            return end