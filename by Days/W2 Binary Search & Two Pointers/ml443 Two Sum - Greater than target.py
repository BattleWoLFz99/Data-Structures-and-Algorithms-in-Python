# count += right - left

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        if not nums:
            return 0

        nums.sort()
        count = 0

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1
            else:
                left += 1

        return count