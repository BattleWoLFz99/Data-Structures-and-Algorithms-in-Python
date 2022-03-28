# TLE if EMPTY >> HOUSE:
DIRECTIONS = ((-1, 0), (1, 0), (0, 1), (0, -1))
class GridType:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] == GridType.EMPTY:
                    distance = self.bfs(grid, i, j)
                    min_dist = min(min_dist, self.get_dist_sum(distance, grid))

        return min_dist if min_dist != float('inf') else -1

    def bfs(self, grid, i, j):
        distance = {(i, j): 0}
        queue = collections.deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(grid, next_x, next_y):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                if grid[next_x][next_y] != GridType.HOUSE:
                    queue.append((next_x, next_y))
        return distance

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        return grid[x][y] != GridType.WALL

    def get_dist_sum(self, distance, grid):
        distance_sum = 0
        for x, row in enumerate(grid):
            for y , val in enumerate(row):
                if val == GridType.HOUSE:
                    if (x, y) not in distance:
                        return float('inf')
                    distance_sum += distance[(x, y)]
        return distance_sum
# But it is really Common Sense: Get house_count first, then see if ==
# To save some space, not gonna paste again.


# if EMPTY >> HOUSE:
DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

class GridType:
    WALL = 2
    HOUSE = 1
    EMPTY = 0


class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortest_distance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        distance_sum, reachable_count, houses_count = {}, {}, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == GridType.HOUSE:
                    self.bfs(grid, i, j, distance_sum, reachable_count)
                    houses_count += 1

        min_distance = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in reachable_count:
                    continue
                if reachable_count[(i, j)] != houses_count:
                    continue
                min_distance = min(min_distance, distance_sum[(i, j)])

        return min_distance if min_distance != float('inf') else -1

    def bfs(self, grid, i, j, distance_sum, reachable_count):
        queue = collections.deque([(i, j)])
        distance = {(i, j): 0}
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(grid, next_x, next_y):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))

                if (next_x, next_y) not in reachable_count:
                    distance_sum[(next_x, next_y)] = 0
                    reachable_count[(next_x, next_y)] = 0
                distance_sum[(next_x, next_y)] += distance[(next_x, next_y)]
                reachable_count[(next_x, next_y)] += 1

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        return grid[x][y] == GridType.EMPTY
