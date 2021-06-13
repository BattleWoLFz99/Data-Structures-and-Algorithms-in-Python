import sys
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        if not nums:
            return 

        nums.sort()
        diff = sys.maxsize
        
        left, right = 0, len(nums)  - 1
        while left < right:
            if nums[left] + nums[right] < target:
                diff = min(diff, target - nums[left] - nums[right])
                left += 1
            else:
                diff = min(diff, nums[left] + nums[right] - target)
                right -= 1

        return diff