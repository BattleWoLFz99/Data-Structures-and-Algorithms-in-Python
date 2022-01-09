class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        if n <= 0:
            return 

        results = []
        self.search(n, [], results)

        return results

    def search(self, n, cols, results):
        # 其 index row为对应 行，value 为 j 对应 col 位置
        # Example 1 cols = [[1], [3], [0], [2]]
        row = len(cols)
        if row == n:
            results.append(self.draw_chessboard(cols))
            return

        for col in range(n):
            if not self.is_valid(cols, col, row):
                continue
            cols.append(col)
            # n = 8 与 n = 9 没关系
            self.search(n, cols, results)
            cols.pop()
            
    def draw_chessboard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
    
    def is_valid(self, cols, col, row):
        # 取出要验证的点与已有的所有点对比
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r + c == row + col or r - c == row - col:
                return False
        return True


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        if n <= 0:
            return 

        visited = {
            'col': set(),
            'sum': set(),
            'diff': set()
        }
        results = []
        self.search(n, [], visited, results)

        return results

    def search(self, n, cols, visited, results):
        # 其 index row为对应 行，value 为 j 对应 col 位置
        # Example 1 cols = [[1], [3], [0], [2]]
        row = len(cols)
        if row == n:
            results.append(self.draw_chessboard(cols))
            return

        for col in range(n):
            if not self.is_valid(cols, col, row, visited):
                continue
            cols.append(col)
            visited['col'].add(col)
            visited['sum'].add(row + col)
            visited['diff'].add(row - col)
            # n = 8 与 n = 9 没关系
            self.search(n, cols, visited, results)
            # 别写成 pop() 啊草
            visited['col'].remove(col)
            visited['sum'].remove(row + col)
            visited['diff'].remove(row - col)
            cols.pop()
            
    def draw_chessboard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
    
    def is_valid(self, cols, col, row, visited):
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if row - col in visited['diff']:
            return False
        return True
