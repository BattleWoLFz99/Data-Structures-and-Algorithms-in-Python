DIRECTIONS_HASH = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1)
}


class MazeGridType:
    SPACE = 0
    WALL = 1


class Solution:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """
    def findShortestWay(self, maze, ball, hole):
        if not ball or not hole or \
            not maze or not maze[0]:
            return "impossible"

        hole_position = (hole[0], hole[1])
        queue = collections.deque([(ball[0], ball[1])])
        distance = {(ball[0], ball[1]): (0, '')}
        while queue:
            x, y = queue.popleft()
            dist, path = distance[(x, y)]
            for direction in DIRECTIONS_HASH:
                new_x, new_y = self.kick_ball(maze, direction, x, y, hole_position)
                new_dist = dist + abs(new_x - x) + abs(new_y - y)
                new_path = path + direction
                if (new_x, new_y) in distance and \
                    distance[(new_x, new_y)] <= (new_dist, new_path):
                    continue
                distance[(new_x, new_y)] = (new_dist, new_path)
                queue.append((new_x, new_y))

        if hole_position in distance:
            return distance[hole_position][1]
        return "impossible"

    def kick_ball(self, maze, direction, x, y, hole_position):
        dx, dy = DIRECTIONS_HASH[direction]
        while (x, y) != hole_position and self.is_valid(x, y, maze):
            x += dx
            y += dy
        if (x, y) == hole_position:
            return x, y
        return x - dx, y - dy
    
    def is_valid(self, x, y, maze):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
            return False
        return maze[x][y] == MazeGridType.SPACE