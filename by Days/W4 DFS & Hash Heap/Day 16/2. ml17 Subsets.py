# 更通用的版本，可推广到非组合类型的代码之中，例如查排列

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
        
    def dfs(self, nums, index, subset, results):
        results.append(list(subset))
        
        # 多嘴一句，初始版本是这样：选了0，不能选1了:
        # if len(subset) > 0 and subset[-1] - 1 >= nums[i] 就 continue
        for i in range(index, len(nums)):
            # [1] => [1,2]
            # 去寻找以 [1,2] 开头的所有子集
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            # [1,2] =>[1]    backtracking, subset是一个内存地址, reference
            subset.pop()


# 上面是手动加进去，再回溯，最后一步再深拷贝
# 若深拷贝，可以省掉回溯：

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
        
    def dfs(self, nums, index, subset, results):
        # results.append(list(subset))
        results.append(subset)
        
        for i in range(index, len(nums)):
            # subset.append(nums[i])
            new_set = list(subset)
            new_set.append(nums[i])
            self.dfs(nums, i + 1, new_set, results)
            # subset.pop()