"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

OFFSETS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]

class Solution:
        
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0]:
            return 0

        queue = collections.deque([(source.x, source.y)])
        dis_to_src_map = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return dis_to_src_map[(x, y)]

            for dx, dy, in OFFSETS:
                next_x = x + dx
                next_y = y + dy
                if not self.is_valid(grid, next_x, next_y, dis_to_src_map):
                    continue
                queue.append((next_x, next_y))
                dis_to_src_map[(next_x, next_y)] = dis_to_src_map[(x, y)] + 1

        return -1

    def is_valid(self, grid, x, y, dis_to_src_map):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in dis_to_src_map:
            return False
        return not grid[x][y]