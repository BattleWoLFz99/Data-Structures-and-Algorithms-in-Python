DIRECTIONS = [
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1),
]

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])
        # state
        f = [[float('inf')] * m for _ in range(n)]

        # initialize:
        f[0][0] = 0

        # function
        # (1, m) 不然滚动数组加不进去
        for j in range(1, m):
            for i in range(n):
                if grid[i][j]:
                    continue
                for delta_x, delta_y in DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        f[i][j] = min(f[i][j], f[x][y] + 1)

        if f[n - 1][m - 1] == float('inf'):
            return -1
        return f[n - 1][m - 1]

# Rolling Array: Day 27/2.~