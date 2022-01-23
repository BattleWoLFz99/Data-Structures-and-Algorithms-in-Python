class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        temp = [0] * len(nums)
        return self.merge_sort(nums, temp, 0, len(nums) - 1)

    def merge_sort(self, nums, temp, start, end):
        if start >= end:
            return 0
        
        count = 0
        mid = (start + end) // 2
        count += self.merge_sort(nums, temp, start, mid)
        count += self.merge_sort(nums, temp, mid + 1, end)
        count += self.merge(nums, temp, start, mid, end)
        return count
    
    def merge(self, nums, temp, start, mid, end):
        left, right = start, mid + 1
        index = start
        
        count = self.count_reverse_pairs(nums, left, right, mid, end)
        
        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                index += 1
                left += 1
            else:
                temp[index] = nums[right]
                index += 1
                right += 1
        while left <= mid:
            temp[index] = nums[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = nums[right]
            index += 1
            right += 1
        for i in range(start, end + 1):
            nums[i] = temp[i]
        
        return count
    
    def count_reverse_pairs(self, nums, left, right, mid, end):
        count = 0
        while left <= mid and right <= end:
            if nums[left] <= 2 * nums[right]:
                left += 1
            else:
                right += 1
                count += mid - left + 1
        return count