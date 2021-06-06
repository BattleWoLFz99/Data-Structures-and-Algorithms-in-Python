# Stoping thinking about mountainSequence Holy... Absolutely different cases
# Biggest problem here: I have seen this before....

class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        k = 0
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[0]:
                end = mid
            elif nums[mid] == nums[0]:
                end = mid
            else:
                start = mid

        if (nums[start] > nums[end]):
            k = start
        else:
            k = end

        if nums[0] == target:
            return 0
        elif nums[0] < target:
            start, end = 0, k
        else:
            start, end = k, len(nums) - 1

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


s = Solution()
print(s.search([5,1,3],1))


# Alter BinarySearchTemplate:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        start, end = 0, len(nums) - 1
        ans = end
        
        # find the rotate value, ans will be 0 in example 1 case
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= nums[0]:
                start, ans = mid + 1, mid
            else:
                end = mid - 1
        
        
        
        # find the corresponding area that target belongs to
        if target >= nums[0]:
            start, end = 0, ans
        else:
            start, end = ans + 1, len(nums) - 1
        
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start, ans = mid + 1, mid
            else:
                end = mid - 1
        
        if nums[ans] == target:
            return ans
        else:
            return -1