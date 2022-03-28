"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        if not node:
            return None

        queue = collections.deque([node])
        visited = set([node])

        while queue:
            curr_node = queue.popleft()
            if values[curr_node] == target:
                return curr_node
            for next_node in curr_node.neighbors:
                if next_node in visited:
                    continue
                queue.append(next_node)
                visited.add(next_node)
        
        return "0v0"
