class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        used = self.build_map(board)
        self.dfs(used, 0, board)

    def build_map(self, board):
        used = {
            'row': [set() for _ in range(9)],
            'col': [set() for _ in range(9)],
            'box': [set() for _ in range(9)]
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    continue
                used['row'][i].add(board[i][j])
                used['col'][j].add(board[i][j])
                used['box'][i // 3 * 3 + j // 3].add(board[i][j])
        
        return used

    def dfs(self, used, index, board):
        if index == 81:
            return True

        i, j = index // 9, index % 9
        if board[i][j] != 0:
            return self.dfs(used, index + 1, board)

        for num in range(1, 10):
            if not self.is_valid(i, j, num, used):
                continue
            
            board[i][j] = num
            used['row'][i].add(num)
            used['col'][j].add(num)
            used['box'][i // 3 * 3 + j // 3].add(num)
            if self.dfs(used, index + 1, board):
                return True
            used['box'][i // 3 * 3 + j // 3].remove(num)
            used['col'][j].remove(num)
            used['row'][i].remove(num)
            board[i][j] = 0
        return False

    def is_valid(self, i, j, num, used):
        if num in used['row'][i]:
            return False
        if num in used['col'][j]:
            return False
        if num in used['box'][i // 3 * 3 + j // 3]:
            return False
        return True


class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        self.dfs(board)

    def dfs(self, board):
        i, j, choices = self.get_least_choices(board)

        if i is None:
            return True
        
        for val in choices:
            board[i][j] = val
            if self.dfs(board):
                return True
            board[i][j] = 0

    def get_least_choices(self, board):
        x, y, choices = None, None, [0] * 10
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue
                vals = []
                for val in range(1, 10):
                    if self.is_valid(board, i, j, val):
                        vals.append(val)
                if len(vals) < len(choices):
                    x, y, choices = i, j, vals
        return x, y, choices

    def is_valid(self, board, x, y, val):
        for i in range(9):
            if board[x][i] == val:
                return False
            if board[i][y] == val:
                return False
            if board[x // 3 * 3 + i // 3][y // 3 * 3 + i % 3] == val:
                return False
        return True