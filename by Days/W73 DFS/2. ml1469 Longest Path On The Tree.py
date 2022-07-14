# V1 DFS Stackoverflow
class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):

        # 建图
        neighbors = {}
        for i in range(n - 1):
            start = starts[i]
            end = ends[i]
            dist = lens[i]

            if start not in neighbors:
                neighbors[start] = []
            if end not in neighbors:
                neighbors[end] = []

            neighbors[start].append((end, dist))
            neighbors[end].append((start, dist))

        chain, path = self.dfs(0, -1, neighbors)
        return path

    def dfs(self, root, parent, neighbors):
        longest_chain = 0
        longest_path = 0

        child_longest_chain = 0
        child_second_longest_chain = 0

        for neighbor, dist in neighbors[root]:
            if neighbor == parent:
                continue
            
            child_chain, child_path = self.dfs(neighbor, root, neighbors)
            child_chain += dist

            longest_path = max(child_path, longest_path)
            longest_chain = max(child_chain, longest_chain)

            _, child_second_longest_chain, child_longest_chain = \
            sorted([child_longest_chain, child_second_longest_chain, child_chain])

        longest_path = max(child_longest_chain + child_second_longest_chain, longest_path)

        return longest_chain, longest_path


# Dual BFS
class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):
        neighbors = {}
        for i in range(n - 1):
            start = starts[i]
            end = ends[i]
            dist = lens[i]

            if start not in neighbors:
                neighbors[start] = []
            if end not in neighbors:
                neighbors[end] = []

            neighbors[start].append((end, dist))
            neighbors[end].append((start, dist))

        # 无向图，随意了，0 to n-1 都ok
        start, _ = self.bfs(0, neighbors)
        end, ans = self.bfs(start, neighbors)
        return ans

    def bfs(self, root, neighbors):
        queue = collections.deque([root])
        distance = {root: 0}
        max_distance = 0
        max_node = -1
        while queue:
            node = queue.popleft()
            if max_distance < distance[node]:
                max_distance = distance[node]
                max_node = node
            for neighbor, edge_length in neighbors[node]:
                if neighbor in distance:
                    continue
                queue.append(neighbor)
                distance[neighbor] = distance[node] + edge_length
        
        return max_node, max_distance