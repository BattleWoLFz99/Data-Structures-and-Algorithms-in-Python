class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        results = []       
        if nums is None:
            return results
        if not nums:
            return [results]

        nums = sorted(nums)
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, index, combination, results):
        results.append(list(combination))
        
        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, results)
            combination.pop()