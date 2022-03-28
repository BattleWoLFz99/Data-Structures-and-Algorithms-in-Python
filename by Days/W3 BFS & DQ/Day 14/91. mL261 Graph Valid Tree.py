# LintCode: Return results
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n < 0:
            return False
        if n != len(edges) + 1:
            return False
        if not edges and n == 1:
            return True

        graph = self.build_graph(edges, n)
        visited = set([0])
        queue = collections.deque([0])
        
        while queue:
            node = queue.popleft()
            visited.add(node)
            for next_node in graph[node]:
                if next_node in visited:
                    continue
                queue.append(next_node)
                visited.add(next_node)

        return len(visited) == n
    
    def build_graph(self, edges, n):
        graph = {
            i: set()
            for i in range(n)
        }
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return graph


# LeetCode: Return how many:
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n < 0:
            return False
        if n != len(edges) + 1:
            return False
        if not edges and n == 1:
            return True

        graph = self.build_graph(edges, n)
        visited = set([0])
        queue = collections.deque([0])
        
        while queue:
            node = queue.popleft()
            visited.add(node)
            for next_node in graph[node]:
                if next_node in visited:
                    continue
                queue.append(next_node)
                visited.add(next_node)

        return len(visited) == n
    
    def build_graph(self, edges, n):
        graph = {
            i: set()
            for i in range(n)
        }
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return graph