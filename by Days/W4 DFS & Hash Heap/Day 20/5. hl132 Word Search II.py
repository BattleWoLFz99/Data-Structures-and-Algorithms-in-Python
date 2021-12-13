DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []
        if board[0] is None or len(board[0]) == 0:
            return[]

        words_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        results_set = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(
                    board,
                    i,
                    j,
                    board[i][j],
                    words_set,
                    prefix_set,
                    set([(i, j)]),
                    results_set
                )

        return list(results_set)

    def dfs(self, board, x, y, word, words_set, prefix_set, visited, results_set):
        if word not in prefix_set:
            return

        if word in words_set:
            results_set.add(word)

        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy
            
            if not self.inside(next_x, next_y, board) or (next_x, next_y) in visited:
                continue

            visited.add((next_x, next_y))
            self.dfs(
                board,
                next_x,
                next_y,
                word + board[next_x][next_y],
                words_set,
                prefix_set,
                visited,
                results_set
            )
            visited.remove((next_x, next_y))


    def inside(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0])


# 更 OI 的写法：
# 其实空间复杂度感觉无所谓了，应该垃圾回收机制了
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []
        if board[0] is None or len(board[0]) == 0:
            return[]

        words_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        results_set = set()
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited[i][j] = True
                self.dfs(
                    board,
                    i,
                    j,
                    board[i][j],
                    words_set,
                    prefix_set,
                    visited,
                    results_set
                )
                visited[i][j] = False

        return list(results_set)

    def dfs(self, board, x, y, word, words_set, prefix_set, visited, results_set):
        if word not in prefix_set:
            return

        if word in words_set:
            results_set.add(word)

        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy
            if not self.inside(next_x, next_y, board) or visited[next_x][next_y]:
                continue

            visited[next_x][next_y] = True
            self.dfs(
                board,
                next_x,
                next_y,
                word + board[next_x][next_y],
                words_set,
                prefix_set,
                visited,
                results_set
            )
            visited[next_x][next_y] = False


    def inside(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0])