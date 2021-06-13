# Given a unsorted array with integers, find the median of it.
# A median is the middle number of the array after it is sorted.
# If there are even numbers in the array, return the N/2-th number after sorted.

# It is (len(nums) - 1) // 2

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        if not nums:
            return 

        return self.quick_select(nums, 0, len(nums) - 1, (len(nums) - 1) // 2)

    def quick_select(self, nums, start, end, target):
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

        if target <= right:
            self.quick_select(nums, start, right, target)
        if target >= left:
            self.quick_select(nums, left, end, target)

        return nums[target]