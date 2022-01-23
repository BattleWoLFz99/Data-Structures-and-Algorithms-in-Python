# n 要 + 1.... 
class Solution:
    """
    Given two integers n and k, return all possible combinations of k numbers 
    out of the range [1, n].
    You may return the answer in any order.
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n:
            return []
        
        combinations = []
        self.dfs(n, k, 1, [], combinations)
        
        return combinations
    
    def dfs(self, n, k, index, combination, combinations):
        if len(combination) == k:
            combinations.append(list(combination))
            return
            
        for i in range(index, n + 1):
            combination.append(i)
            self.dfs(n, k, i + 1, combination, combinations)
            combination.pop()