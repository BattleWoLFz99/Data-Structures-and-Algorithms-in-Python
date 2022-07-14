class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        combinations = []

        if not candidates:
            return [combinations]
        # 没有重复元素则不需要去重，就不用 sort
        unique_sorted_numbers = sorted(list(set(candidates)))
        self.dfs(unique_sorted_numbers, 0, target, [], combinations)
        return combinations

    # 递归的定义：有 unique_sorted_numbers[index ... n-1] 这些数可以选
    # 他们的目标和视 target，每选一个数 target 就减掉这个数传入下层
    # 我现在可以从 index 这个位置开始选，每次选完这个数还是可以继续选这个数，不用 + 1
    # combination 是当前的组合，找到了就放到 results 里面
    def dfs(self, unique_sorted_numbers, index, target, combination, combinations):
        if target < 0:
            return
        
        if target == 0:
            combinations.append(list(combination))
            return 
            
        # 递归的拆解：挑一个数放到 combination 里
        for i in range(index, len(unique_sorted_numbers)):
            combination.append(unique_sorted_numbers[i])
            # 传入 i 而不是 i + 1，代表下一层 dfs 可以使用重复位置的数字
            self.dfs(
                unique_sorted_numbers,
                i,
                target - unique_sorted_numbers[i],
                combination,
                combinations
            )
            combination.pop()