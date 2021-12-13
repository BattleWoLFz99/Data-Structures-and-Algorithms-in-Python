class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        chars = sorted(list(str))
        visited = [False] * len(chars)
        permutations = []
        self.dfs(chars, visited, [], permutations) 
        return permutations

    # 递归的定义: 找到所有 permutation 开头的排列
    def dfs(self, chars, visited, permutation, permutations):
        # 递归的出口：当我找到一个完整的排列
        if len(chars) == len(permutation):
            permutations.append(''.join(permutation))
            return    
        
        # 递归的拆解：基于当前的前缀，下一个字符放啥
        for i in range(len(chars)):
            # 同一个位置上的字符用过不能在用
            if visited[i]:
                continue
            # 去重：不同位置的同样的字符，必须按照顺序用。
            # a' a" b
            # => a' a" b => √
            # => a" a' b => x
            # 不能跳过一个a选下一个a
            if i > 0 and chars[i] == chars[i - 1] and not visited[i - 1]:
                continue

            permutation.append(chars[i])
            visited[i] = True
            self.dfs(chars, visited, permutation, permutations)
            visited[i] = False
            permutation.pop()