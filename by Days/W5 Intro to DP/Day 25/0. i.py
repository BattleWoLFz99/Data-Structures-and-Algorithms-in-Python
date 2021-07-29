class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def template(self, nums):
        if not nums:
            return 0

        # nums.sort()
        j = 1
        for i in range(len(nums)):
            while j < len(nums) and i, j的搭配不满足条件:
                j += 1
            if j >= len(nums):
                break
            处理 i, j 这次搭配

        return