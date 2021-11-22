class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permuteUnique(self, nums):
        if not nums:
            return [[]]

        nums.sort()
        permutations = []
        # visited = [0] * len(nums)
        visited = [0 for _ in range(len(nums))]
        self.dfs(nums, visited, [], permutations)

        return permutations

    def dfs(self, nums, visited, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            # i位置这个元素已经被用过
            if visited[i]:
                continue
            # 首先前面得有数 i大于0 and 当前的数和前面的数一样 and 前面的数没用过
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            permutation.append(nums[i])
            visited[i] = 1
            self.dfs(nums, visited, permutation, permutations)
            visited[i] = 0
            permutation.pop()