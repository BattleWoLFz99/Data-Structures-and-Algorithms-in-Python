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
        self.dfs(root, path, results, 0,  target)

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