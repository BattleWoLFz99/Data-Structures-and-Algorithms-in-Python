# LeetCode 版：反正就那句话挺对的，写多了，就这么写好没什么什么版本什么版本的。。

DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words or not board or not board[0]:
            return []
        
        prefix_set = self.get_prefix_set(words)
        words_set = set(words)
        result_set = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, prefix_set, words_set, set([(i, j)]), \
                         i, j, board[i][j], result_set)
                
        return result_set
    
    def get_prefix_set(self, words):
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i])
                
        return prefix_set
    
    def dfs(self, board, prefix_set, words_set, visited, \
                  x, y, path, result_set):
        if path in words_set:
            result_set.add(str(path))
            # got "app", maybe has "apple", cant return now

        if path not in prefix_set:
            return
        
        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy
            if not self.is_valid(next_x, next_y, board, visited):
                continue
            visited.add((next_x, next_y))
            self.dfs(board, prefix_set, words_set, visited, \
                     next_x, next_y, path + board[next_x][next_y], result_set)
            visited.remove((next_x, next_y))
            
    def is_valid(self, x, y, board, visited):
        n, m = len(board), len(board[0])
        if (x, y) in visited:
            return False
        if not (0 <= x < n and 0 <= y < m):
            return False
        return True