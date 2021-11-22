'''
Given two integers n and k, return all possible combinations of k numbers 
out of the range [1, n]. You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:  
        nums = [x for x in range(1, n + 1)]
        combinations = []
        self.dfs(k, nums, 0, [], combinations)
        
        return combinations
    
    def dfs(self, k, nums, index, combination, combinations):
        if len(combination) == k:
            combinations.append(list(combination))
            return
        
        for i in range(index, len(nums)):
            # if i > index and nums[i] == nums[i - 1]:
                # continue
                
            combination.append(nums[i])
            self.dfs(k, nums, i + 1, combination, combinations)
            combination.pop()