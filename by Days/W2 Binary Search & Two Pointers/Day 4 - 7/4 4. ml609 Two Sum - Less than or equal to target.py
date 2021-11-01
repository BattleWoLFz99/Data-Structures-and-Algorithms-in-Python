class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            count += right - left
            left += 1

        return count