class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(connections)
        # ans: set of edges, small to big
        ans = set(map(tuple, map(sorted, connections)))
        rank = [float('-inf')] * n
        self.dfs(0, 0, rank, graph, ans, n)
        
        return ans

    def dfs(self, node, depth, rank, graph, ans, n):
        # 返回的是 DFS序！
        if rank[node] >= 0:
            return rank[node]
        
        rank[node] = depth
        min_dfs_depth = n
        for neighbor in graph[node]:
            if rank[neighbor] == depth - 1:
                continue
                
            dfs_depth = self.dfs(neighbor, depth + 1, rank, graph, ans, n)
            if dfs_depth <= rank[node]:
                # remove will raise error if not find. discard does not.
                # BUT DO NOT USE discard! If raised, means error!!
                # sorted(tuple) return a list, tuple() again
                ans.discard(tuple(sorted((neighbor, node))))
            min_dfs_depth = min(min_dfs_depth, dfs_depth)

        return min_dfs_depth
    
    def build_graph(self, connections):
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        return graph
    
        