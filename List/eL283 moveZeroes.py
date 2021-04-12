# move non-zero numbers to the front, then 0 for the rest...
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for num in nums:
            if num != 0:
                nums[count] = num
                count += 1
        for i in range(count, len(nums)):
            nums[i] = 0

# just swap...
class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """
    def moveZeroes(self, nums):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                # temp is not needed
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1