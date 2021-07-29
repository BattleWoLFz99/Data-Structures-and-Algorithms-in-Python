class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if not nums:
            return 0
            
        nums.sort()
        j = 1
        for i in range(len(nums)):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j >= len(nums):
                break
            nums[i + 1] = nums[j]

        return i + 1
        