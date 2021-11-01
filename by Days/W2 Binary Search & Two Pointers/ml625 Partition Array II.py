class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < low:
                left += 1
            while left <= right and nums[right] >= low:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] <= high:
                left += 1
            while left <= right and nums[right] > high:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1