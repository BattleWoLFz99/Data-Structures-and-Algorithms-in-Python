# 一路 if，因为图方便 path 里直接扔 val
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
            
        paths = []
        self.dfs(root, [root.val], paths, target)
        return paths
        
    def dfs(self, node, path, paths, target):
        if not node.left and not node.right:
            if sum(path) == target:
                paths.append(list(path))
            return
        
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, path, paths, target)
            path.pop()
        
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, path, paths, target)
            path.pop()