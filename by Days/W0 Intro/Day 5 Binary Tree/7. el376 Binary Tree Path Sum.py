# Line 29 不能加 return，因为被夹在append pop之间了
# Also for el480
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        results = []
        path = []
        self.dfs(root, path, results, 0, target)

        return results

    def dfs(self, root, path, results, length, target):
        if root is None:
            return
        path.append(root.val)
        length += root.val

        if root.left is None and root.right is None and length == target:
            results.append(list(path))

        self.dfs(root.left, path, results, length, target)
        self.dfs(root.right, path, results, length, target)
        path.pop()


# From el480 Version 2.
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
            
        result = []
        self.dfs(root, [root.val], result, target)
        return result
        
    def dfs(self, node, path, result, target):
        if not node.left and not node.right:
            if sum(path) == target:
                result.append(list(path))
            return
        
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, path, result, target)
            path.pop()
        
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, path, result, target)
            path.pop()