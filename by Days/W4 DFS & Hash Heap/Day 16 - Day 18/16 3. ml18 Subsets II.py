# 更通用的版本，每一层代表可选哪一个。
# 可推广到非组合类型的代码之中，例如查排列

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        results = []       
        if not nums:
            return [results]

        nums = sorted(nums)
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, index, subset, results):
        results.append(list(subset))
        
        for i in range(index, len(nums)):
            # if i > 0 and nums[i] == nums[i - 1] and i != index:
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()


# or using hash:

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        subsets = []
        visited = {}
        nums.sort()
        self.dfs(nums, 0, [], subsets, visited)
        
        return subsets

    def get_hash(self, subset):
        hash_string = "-".join([str(num) for num in subset])
        return hash_string
        
    def dfs(self, nums, start_index, subset, subsets, visited):
        hash_string = self.get_hash(subset)
        if hash_string in visited:
            return
        
        visited[hash_string] = True
        subsets.append(list(subset))
        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets, visited)
            subset.pop()