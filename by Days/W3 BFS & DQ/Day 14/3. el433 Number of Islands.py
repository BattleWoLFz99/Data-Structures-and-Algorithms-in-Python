# Try NOT to change the original input

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        visited = set()
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j] or (i, j) in visited:
                    continue
                self.bfs(grid, i, j, visited)
                islands += 1

        return islands

    def bfs(self, grid, x, y, visited):
        # 固定搭配包一层 []
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        while queue:
            # tuple 直接 pop
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        # 写传统 if 放这里，上面会list out of range
        return grid[x][y]

