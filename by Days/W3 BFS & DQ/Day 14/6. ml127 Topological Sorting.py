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
        in_degree = self.get_indegree(graph)

        # 2. 0扔queue
        queue = collections.deque()
        for n in graph:
            if in_degree[n] == 0:
                queue.append(n)

        # 记录
        order = []
        while queue:
            # 3. 拿出
            curr = queue.popleft()
            order.append(curr)
            for neighbor in curr.neighbors:
                in_degree[neighbor] -= 1
                # 4. 0扔queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order


    def get_indegree(self, graph):
        in_degree = {x:0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                in_degree[neighbor] += 1

        return in_degree