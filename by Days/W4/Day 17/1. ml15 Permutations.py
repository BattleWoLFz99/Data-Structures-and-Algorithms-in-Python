class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # 如果数组为空直接返回空
        if nums is None:
            return []

        if not nums:
            return [[]]

        permutations = []
        visited = [0] * len(nums)
        self.dfs(nums, visited, [], permutations)

        return permutations

    # 递归的定义: 找到所有permutation 开头的 permutations
    def dfs(self, nums, visited, permutation, permutations):
        #  递归的出口: 找到一组排列，已到达边界条件
        if len(nums) == len(permutation):
            # 因为地址传递，在最终回溯后current为空导致results中均为空列表
            # 所以不能写成results.append(current)
            permutations.append(list(permutation))
            return

        # 递归的拆解
        # [] -> [1], [2], [3]
        # [1] -> [1, 2], [1, 3], [1, 4]...
        for i in range(len(nums)):
            # i位置这个元素已经被用过
            if visited[i]:
                continue
            # 继续递归
            permutation.append(nums[i])
            visited[i] = 1
            self.dfs(nums, visited, permutation, permutations)
            visited[i] = 0
            permutation.pop()