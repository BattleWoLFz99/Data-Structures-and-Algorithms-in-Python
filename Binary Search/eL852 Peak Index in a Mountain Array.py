class Solution:
    def peakIndexInMountainArray(self, arr):
        if arr is None:
            return -1

        start, end = 0, len(arr) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] < arr[mid + 1]:
                start = mid
            else:
                end = mid
        if arr[start] > arr[start + 1] and arr[start] > arr[start - 1]:
            return start
        else:
            return end

s = Solution()
print(s.peakIndexInMountainArray([5,1,3]))
        # DO NOT if end >= len(arr) - 1 or arr[end] > arr[end + 1]
        # or it would be a huge trouble for the following questions.