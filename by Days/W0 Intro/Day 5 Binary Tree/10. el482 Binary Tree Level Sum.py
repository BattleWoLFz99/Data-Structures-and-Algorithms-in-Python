# 某层节点，BFS是最好的
# 非递归：
    def level_sum(self, root: TreeNode, level: int) -> int:
        if not root or level <= 0:
            return 0

        queue = collections.deque([root])
        results = []

        while queue:
            results.append([node.val for node in queue])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        if level - 1 >= len(results):
            return 0
        return sum(results[level - 1])


    def levelSum(self, root, level):
        # Write your code here
        nodes = []
        self.dfs(root, nodes, 1, level)
        return sum(nodes)

    def dfs(self, root, nodes, dep, level):
        if root is None:
            return
        if dep == level:
            p.append(root.val)
            return
    
        self.dfs(root.left, nodes, dep + 1, level)
        self.dfs(root.right, nodes, dep + 1, level)