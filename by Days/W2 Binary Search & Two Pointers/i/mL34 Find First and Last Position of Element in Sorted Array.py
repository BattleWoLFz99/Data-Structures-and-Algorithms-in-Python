# 更简单的记忆方法是只记 First 的简化版，然后 Last 推出来:
# First 起手start，收手start, end 带等于
# 就大概不会忘了带 elif 了吧草。。

    def firstPosition(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target: 
            return end
        return -1


# First SEE-SE, Last SSE-ES
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        start, end = 0, len(nums) - 1
        
        return (self.firstPosition(nums, start, end, target), self.lastPosition(nums, start, end, target))
        
    def firstPosition(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target: 
            return end
        return -1

    def lastPosition(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                start = mid
            else:
                end = mid

        if nums[end] == target: 
            return end
        if nums[start] == target:
            return start
        return -1