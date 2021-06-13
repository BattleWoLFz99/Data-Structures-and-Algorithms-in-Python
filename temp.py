class Solution:
    def median(self, nums):
        if not nums:
            return  
            
        return self.partition(nums, 0, len(nums) - 1, (len(nums) - 1) // 2)
        
    def partition(self, nums, start, end, k):
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
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
            
        return nums[k]