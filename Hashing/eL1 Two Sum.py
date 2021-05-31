# Modified, return two values:

class Solution:
    def twoSum(self, numbers, target):
        hashset = set()
        for ele in numbers:
            if target - ele in hashset:
                return ele, target - ele
            hashset.add(ele)
        return [-1, -1] 

# Leetcode Ver.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [i, hash[target - nums[i]]]
            hash[nums[i]] = i
#       return [-1, -1]




        