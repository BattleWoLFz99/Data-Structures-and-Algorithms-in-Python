class Solution:
    def mountainSequence(self, nums):
        # write your code here
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid

        return max(nums[start], nums[end])

s = Solution()
print(s.mountainSequence([5,1,3]))
# DO NOT do the following:
"""
        if start >= len(nums) - 1 or nums[start] > nums[start + 1]:
            return nums[start]
        # if end >= len(nums) - 1 or nums[end] > nums[end + 1]:   
        if nums[end] > nums[end + 1]:
            return nums[end]
"""