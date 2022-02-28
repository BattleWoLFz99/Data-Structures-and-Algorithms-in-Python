# 先 partition，再交错

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, nums):
        if not nums:
            return []
        
        neg_count = self.partition(nums)
        pos_count = len(nums) - neg_count
        print(neg_count, pos_count)
        if neg_count > pos_count:
            self.switch(nums, 1, len(nums) - 1)
        elif neg_count == pos_count:
            self.switch(nums, 1, len(nums) - 2)
        else:
            self.switch(nums, 0, len(nums) - 2)
        
    def partition(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < 0:
                left += 1
            while left <= right and nums[right] > 0:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        return right + 1
                
    def switch(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 2
            right -=2
