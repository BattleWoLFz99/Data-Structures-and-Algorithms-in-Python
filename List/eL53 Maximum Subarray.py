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

