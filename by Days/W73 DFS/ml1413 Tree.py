from typing import (
    List,
)

class Solution:
    """
    @param x: The x
    @param y: The y
    @param a: The a
    @param b: The b
    @return: The Answer
    """
    def tree(self, x: List[int], y: List[int], a: List[int], b: List[int]) -> List[int]:
        graph = self.build_graph(x, y)
        parent = self.build_tree(1, graph)

        results = []
        for u, v in zip(a, b):
            if parent[v] == parent[u]:
                results.append(1)
            elif parent[v] == u or parent[u] == v:
                results.append(2)
            else:
                results.append(0)

        return results

    def build_graph(self, x, y):
        graph = {}
        for u, v in zip(x, y):
            if u not in graph:
                graph[u] = set()
            if v not in graph:
                graph[v] = set()
            graph[u].add(v)
            graph[v].add(u)

        return graph

    def build_tree(self, root_val, graph):
        queue = collections.deque([root_val])
        visited = set([root_val])
        parent = {root_val: None}
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = node
        
        return parent
                
