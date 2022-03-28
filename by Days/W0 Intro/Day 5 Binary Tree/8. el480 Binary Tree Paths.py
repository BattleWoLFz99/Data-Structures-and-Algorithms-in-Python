# 为了降低出 BUG 几率，统一使用 if left if right
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if root is None:
            return []
            
        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()  # 回溯
        
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()


# 暂时不看这个
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []

        path = []
        results = []
        self.dfs(root, path, results)

        return results

    def dfs(self, root, path, results):
        if root is None:
            return

        path.append(root.val)

        if root.left is None and root.right is None:
            results.append('->'.join([str(n) for n in path]))

        self.dfs(root.left, path, results)
        self.dfs(root.right, path, results)
        path.pop()


# 反面教材，不用DFS遍历法去求具体路径
    def binaryTreePaths(self, root):
        if root is None:
            return []
            
        # 99% 的题，不用单独处理叶子节点
        # 这里需要单独处理的原因是 root 是 None 的结果，没有办法用于构造 root 是叶子的结果
        if root.left is None and root.right is None:
            return [str(root.val)]

        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        paths = []
        for path in leftPaths + rightPaths:
            paths.append(str(root.val) + '->' + path)
            
        return paths