from typing import (
    List,
)
DIRECTIONS = ((0, -1), (-1, 0), (1, 0), (0, 1))

class MatrixType:
    WALL = 2
    ZOMBIE = 1
    HUMAN = 0

class Solution:
    def zombie(self, grid: List[List[int]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()
        human_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == MatrixType.ZOMBIE:
                    visited.add((i, j))
                    queue.append((i, j))
                if grid[i][j] == MatrixType.HUMAN:
                    human_count += 1

        days = 0
        affected_count = 0
        while queue:
            if affected_count >= human_count:
                return days
            days += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in visited:
                        continue
                    if not self.is_valid(next_x, next_y, grid):
                        continue
                    affected_count += 1
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

        return -1

    def is_valid(self, x, y, grid):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        return grid[x][y] == MatrixType.HUMAN