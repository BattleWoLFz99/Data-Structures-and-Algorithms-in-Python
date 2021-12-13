# 组合一定带 index，不需要起手排序， 除非说要排序输出
class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        if not A:
            return [[]]

        combinations = []
        self.dfs(A, k, 0, target, [], combinations)

        return combinations

    def dfs(self, A, k, index, target, combination, combinations):
        if k == 0 and target == 0:
            combinations.append(list(combination))
            return

        if k <= 0 or target < 0:
            return

        for i in range(index, len(A)):
            combination.append(A[i])
            self.dfs(A, k - 1, i + 1, target - A[i], combination, combinations)
            combination.pop()