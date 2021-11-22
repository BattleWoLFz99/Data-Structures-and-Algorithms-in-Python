# 标准组合类的DFS搜索问题解。每一层代表选与不选
# 所以二叉，必须走到叶子节点。所有叶子节点是结果，所以用长度判断返回

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        results = []
        if not nums:
            return [results]

        nums.sort()
        self.dfs(nums, 0, [], results)
        return results

    # 1. 递归的定义
    def dfs(self, nums, index, subset, results):
        # 3. 递归的出口
        if index == len(nums):
            results.append(list(subset))
            return

        # 2. 递归的拆解
        # 选 nums[index]
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, results)

        # 不选 nums[index]
        subset.pop()
        self.dfs(nums, index + 1, subset, results)