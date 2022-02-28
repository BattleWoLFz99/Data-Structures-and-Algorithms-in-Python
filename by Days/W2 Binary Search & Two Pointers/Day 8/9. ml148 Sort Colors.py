# QuickSort is slower, dont
# Counting Sort ver.
# Uses extra space:
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        if nums is None or len(nums) == 0:
            return

        color_cnts = [0] * 3
        for num in nums:
            color_cnts[num] += 1
        
        index = 0

        for i in range(len(color_cnts)):
            cnt = color_cnts[i]
            while cnt > 0:
                nums[index] = i
                cnt -= 1
                index += 1

# Quick Sort practice:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        self.partition(nums, 0)
        self.partition(nums, 1)
        
    def partition(self, nums, pivot):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

# or, it increases your logic complexity, do this only as follow-up(or never)
# One Traversal:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        n = len(nums)
        two_pointer, zero_pointer, i = n, -1, 0
        while zero_pointer < n and i < two_pointer:
            if nums[i] == 0:
                zero_pointer += 1
                nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
            elif nums[i] == 2:
                two_pointer -= 1
                nums[two_pointer], nums[i] = nums[i], nums[two_pointer]
                i -= 1
            i += 1