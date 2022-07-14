from typing import (
    List,
)

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
             we will sort your return value in output
    """
    def generate_parenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        
        results = []
        self.dfs(n, 0, [], results)
        return results
    
    # n: how many Parentheses left
    def dfs(self, n, left_count, sequence, results):
        if len(sequence) == 2 * n:
            results.append(''.join(sequence))
            return

        # add '(', 这才是剪枝，而且是自己后面想到的结果写成令狐的样子
        if left_count < n:
            sequence.append('(')
            self.dfs(n, left_count + 1, sequence, results)
            sequence.pop()

        # add ')' 这不是剪枝，剪枝不影响程序正确性，这个剪了就 ))(( 了
        if left_count > len(sequence) - left_count:
            sequence.append(')')
            self.dfs(n, left_count, sequence, results)
            sequence.pop()