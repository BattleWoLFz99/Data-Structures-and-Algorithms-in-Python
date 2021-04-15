# TLE Version 1:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        idx1 = 0
        idx2 = 0
        s = []
        while idx1 < len(nums):
            while idx2 <len(nums):
                newlist = nums[idx1:idx2+1]
                list_sum = sum(newlist)
                s.append(list_sum)
                idx2+=1
            idx1 += 1
            idx2 = idx1
        return max(s)

# TLE Version 2, without storing the sum in a list:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        idx1 = 0
        idx2 = 0
        # !! maxsum = -math.inf
        maxsum = nums[0]
        while idx1 < len(nums):
            while idx2 <len(nums):
                currentsum = sum(nums[idx1:idx2+1])
                maxsum = max(currentsum, maxsum)
                idx2+=1
            idx1 += 1
            idx2 = idx1
        return maxsum

# TLE Version 3, no need to create a list (I still prefer to use 2 pointers, for practice)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray

# Version 4 DP: Have not learned that far...

# Version 5 D&C: Have not learned that far...
