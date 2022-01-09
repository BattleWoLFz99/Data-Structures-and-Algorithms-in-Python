DIRECTIONS = (
    (1, 2), (1, -2), (-1, 2), (-1, -2),
    (2, 1), (2, -1), (-2, 1), (-2, -1)
)

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0]:
            return -1
        if grid[destination.x][destination.y]:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0

        forward_queue = collections.deque([(source.x, source.y)])
        forward_set = set([(source.x, source.y)])
        backward_queue = collections.deque([(destination.x, destination.y)])
        backward_set = set([(destination.x, destination.y)])

        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(grid, forward_queue, forward_set, backward_set):
                return distance

            distance += 1
            if self.extend_queue(grid, backward_queue, backward_set, forward_set):
                return distance

        return -1

    def extend_queue(self, grid, queue, visited, target_set):
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