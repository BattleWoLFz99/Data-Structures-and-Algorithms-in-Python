class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        if n <= 0:
            return 0
    
        return self.search(n, [])
    
    def search(self, n, cols):
        row = len(cols)
        if row == n:
            return 1
        
        count = 0
        for col in range(n):
            if not self.is_valid(row, col, cols):
                continue
            cols.append(col)
            count += self.search(n, cols)
            cols.pop()
        return count
            
    def is_valid(self, row, col, cols):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if row + col == r + c:
                return False
            if row - col == r - c:
                return False
        return True


class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        if n <= 0:
            return 

        visited = {
            'col': set(),
            'sum': set(),
            'diff': set()
        }

        return self.search(n, [], visited)

    def search(self, n, cols, visited):
        row = len(cols)
        if row == n:
            return 1

        count = 0
        for col in range(n):
            if not self.is_valid(cols, col, row, visited):
                continue
            cols.append(col)
            visited['col'].add(col)
            visited['sum'].add(row + col)
            visited['diff'].add(row - col)
            count += self.search(n, cols, visited)
            visited['col'].remove(col)
            visited['sum'].remove(row + col)
            visited['diff'].remove(row - col)
            cols.pop()

        return count
    
    def is_valid(self, cols, col, row, visited):
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if row - col in visited['diff']:
            return False
        return True

