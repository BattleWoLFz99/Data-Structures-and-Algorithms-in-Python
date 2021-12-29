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

# 所以写到21年底才知道怎么写二分？
# 想找什么就放在第一个if
# 找 first 例如要 min 往前走 等于给了 end，找 last 例如要 max 往后走 等于给了 start
    def woodCut(self, L, k):
        if not L:
            return 0

        start, end = 1, min(max(L), sum(L) // k)
        if end < 1:
            return 0
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_valid(L, k, mid):
                start = mid
            else:
                end = mid
        if self.is_valid(L, k, end):
            return end
        if self.is_valid(L, k, start):
            return start
        return 0

    def is_valid(self, L, k, length):
        pieces = 0
        for i in range(len(L)):
            pieces += L[i] // length
        return pieces >= k

# 找最后，也就是
    def lastPosition(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target: 
            return end
        if nums[start] == target:
            return start
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