# V1: two BFS
class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        graph = self.build_graph(length, connections)
        queue = collections.deque([1])
        distance = {1: 0}
        while queue:
            node = queue.popleft()
            # < right limit
            limit = min(node + 7, length + 1)
            for neighbor in range(node + 1, limit):
                for next_node in self.get_next_nodes(neighbor, graph, distance):
                    if next_node == length:
                        return distance[node] + 1
                    queue.append(next_node)
                    distance[next_node] = distance[node] + 1
        return "???"

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for from_node, to_node in connections:
            graph[from_node].add(to_node)
        return graph

    def get_next_nodes(self, node, graph, distance):
        next_nodes = set()
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            if node in distance:
                continue
            next_nodes.add(node)
            for neighbor in graph[node]:
                if neighbor in distance:
                    continue
                queue.append(neighbor)
                next_nodes.add(neighbor)
        return next_nodes


# V2: SPFA
class Solution:
    def modernLudo(self, length, connections):
        graph = self.build_graph(length, connections)
        queue = collections.deque([1])
        distance = {
            i: float('inf')
            for i in range(1, length + 1)
        }
        distance[1] = 0
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                # 还是写 continue 吧。。不然这套模板题过不了别的题
                # 反着写不好吗？！！！
                # if next_node in distance
                # next_node_is_visited_node <= new_node(curr_node + 0)
                if distance[next_node] <= distance[node]:
                    continue
                distance[next_node] = distance[node]
                queue.append(next_node)

            # < right limit
            right_limit = min(node + 7, length + 1)
            for next_node in range(node + 1, right_limit):
                if distance[next_node] <= distance[node] + 1:
                    continue
                distance[next_node] = distance[node] + 1
                queue.append(next_node)
        return distance[length]

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for from_node, to_node in connections:
            graph[from_node].add(to_node)
        return graph


# V3: SPFA heapq
import heapq
class Solution:
    def modernLudo(self, length, connections):
        graph = self.build_graph(length, connections)
        queue = [(0, 1)]
        distance = {
            i: float('inf')
            for i in range(1, length + 1)
        }
        distance[1] = 0
        while queue:
            dist, node = heapq.heappop(queue)
            for next_node in graph[node]:
                if distance[next_node] <= dist:
                    continue
                distance[next_node] = dist
                heapq.heappush(queue, (dist, next_node))

            # < right limit
            right_limit = min(node + 7, length + 1)
            for next_node in range(node + 1, right_limit):
                if distance[next_node] <= dist + 1:
                    continue
                distance[next_node] = dist + 1
                heapq.heappush(queue, (dist + 1, next_node))
        return distance[length]


# V4: dp[i] = from 1 min_steps to i
    def modernLudo(self, length, connections):
        # V4 dp
        graph = self.build_graph(length, connections)
        # state: dp[i] = from 1 min_steps to i
        # init:
        dp = [float('inf')] * (length + 1)
        dp[length] = 0
        # func:
        for from_node in range(length - 1, 0, -1):
            # < right_limit
            right_limit = min(from_node + 7, length + 1)
            for to_node in range(from_node + 1, right_limit):
                dp[from_node] = min(dp[from_node], dp[to_node] + 1)
            for to_node in graph[from_node]:
                dp[from_node] = min(dp[from_node], dp[to_node])
        return dp[1]

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for from_node, to_node in connections:
            graph[from_node].add(to_node)
        return graph


# V5: dp[i] = from i min_steps to length 
    def modernLudo(self, length, connections):
        # V5 dp
        graph = self.build_graph(length, connections)
        # state: dp[i] = from i min_steps to length
        # init:
        dp = [float('inf')] * (length + 1)
        dp[1] = 0
        # func:
        for to_node in range(2, length + 1):
            # left_limit >=
            left_limit = max(to_node - 6, 1)
            for from_node in range(left_limit, to_node):
                dp[to_node] = min(dp[to_node], dp[from_node] + 1)
            for to_node in graph[from_node]:
                dp[to_node] = min(dp[to_node], dp[from_node])
        return dp[length]

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for from_node, to_node in connections:
            graph[from_node].add(to_node)
        return graph