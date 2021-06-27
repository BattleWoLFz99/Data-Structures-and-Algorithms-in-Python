"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # 1. 建图
        node_to_indegree = self.get_indegree(graph)

        # 2. 0扔queue
        queue = collections.deque()
        for n in graph:
            if node_to_indegree[n] == 0:
                queue.append(n)

        # 记录
        order = []
        while queue:
            # 3. 拿出
            curr = queue.popleft()
            order.append(curr)
            for neighbor in curr.neighbors:
                node_to_indegree[neighbor] -= 1
                # 4. 0扔queue
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order


    def get_indegree(self, graph):
        node_to_indegree = {x:0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1

        return node_to_indegree