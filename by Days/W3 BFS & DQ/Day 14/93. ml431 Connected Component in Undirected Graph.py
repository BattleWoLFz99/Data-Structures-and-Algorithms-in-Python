from typing import (
    List,
)
from lintcode import (
    UndirectedGraphNode,
)

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        # write your code here
        if not nodes:
            return 

        visited = set()
        results = []
        for node in nodes:
            if node in visited:
                continue
            result = []
            self.bfs(node, visited, nodes, result)
            results.append(sorted(result))

        return results

    def bfs(self, node, visited, nodes, result):
        queue = collections.deque([node])
        visited.add(node)
        while queue:
            curr_node = queue.popleft()
            result.append(curr_node.label)
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)