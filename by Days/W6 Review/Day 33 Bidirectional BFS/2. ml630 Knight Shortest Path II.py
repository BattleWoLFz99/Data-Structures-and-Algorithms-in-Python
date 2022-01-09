FORWARD_DIRECTIONS = ((1, 2), (2, 1), (-1, 2), (-2, 1))
BACKWARD_DIRECTIONS = ((1, -2), (-1, -2), (2, -1), (-2, -1))

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        if grid[n - 1][m - 1]:
            return -1
        if (0, 0) == (n - 1, m - 1):
            return 0

        forward_queue = collections.deque([(0, 0)])
        forward_set = set([(0, 0)])
        backward_queue = collections.deque([(n - 1, m - 1)])
        backward_set = set([(n - 1, m - 1)])

        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(grid, forward_queue, forward_set, backward_set, FORWARD_DIRECTIONS):
                return distance

            distance += 1
            if self.extend_queue(grid, backward_queue, backward_set, forward_set, BACKWARD_DIRECTIONS):
                return distance

        return -1

    def extend_queue(self, grid, queue, visited, target_set, DIRECTIONS):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(grid, visited, next_x, next_y):
                    continue
                if (next_x, next_y) in target_set:
                    return True
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
        return False

    def is_valid(self, grid, visited, x, y):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if grid[x][y] == 1:
            return False
        if (x, y) in visited:
            return False
        return True
