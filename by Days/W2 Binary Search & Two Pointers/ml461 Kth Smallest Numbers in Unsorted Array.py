class Solution:
    """
    @param: k: An integer
    @param: nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        return self.quick_select(0, len(nums) - 1, nums, k - 1)
        
    def quick_select(self, start, end, nums, k):
        if start == end:
            return nums[start]
            
        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            self.quick_select(start, right, nums, k)
        if k >= left:
            self.quick_select(left, end, nums, k)
            
        return nums[k]