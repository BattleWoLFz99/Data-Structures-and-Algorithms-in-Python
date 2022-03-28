from typing import (
    List,
)
DIRECTIONS = ((0, -1), (-1, 0), (1, 0), (0, 1))

class GridType:
    HOLE = -1
    ICE = 0
    SNOWBANK = 1
    

class Solution:
    def lake_escape(self, side_length: int, lake_grid: List[List[int]], albert_row: int, albert_column: int, kuna_row: int, kuna_column: int) -> bool:
        # write your code here
        # BFS，起手一定是想起点能不能是终点
        queue = collections.deque([(albert_row, albert_column)])
        visited = set([(albert_row, albert_column)])

        while queue:
            x, y = queue.popleft()
            # print(x, y)
            for dx, dy in DIRECTIONS:
                next_x, next_y = self.get_next_point(x, y, dx, dy, lake_grid)
                if (next_x, next_y) == (-1, -1):
                    continue
                if (next_x, next_y) in visited:
                    continue
                if lake_grid[next_x][next_y] == GridType.SNOWBANK:
                    queue.append((next_x, next_y))
                visited.add((next_x, next_y))

        if not self.can_escape(lake_grid, visited):
            return False
        if (kuna_row, kuna_column) not in visited:
            return False
        return True

    def can_escape(self, lake_grid, visited):
        for i in range(len(lake_grid)):
            if (0, i) in visited or (i, 0) in visited:
                return True
        return False
                
    def get_next_point(self, x, y, dx, dy, lake_grid):
        while 0 <= x + dx < len(lake_grid) and 0 <= y + dy < len(lake_grid[0]):
            x += dx
            y += dy
            if lake_grid[x][y] == GridType.ICE:
                continue
            if lake_grid[x][y] == GridType.HOLE:
                return -1, -1
            break
        return x, y
