"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        if not root:
            return 0

        leaf_val = []
        self.dfs(root, leaf_val)

        return sum(leaf_val)

    def dfs(self, node, leaf_val):
        if not node:
            return
        
        if node.left is None and node.right is None:
            leaf_val.append(node.val)

        self.dfs(node.left, leaf_val)
        self.dfs(node.right, leaf_val)
        

# shorter:
    def leafSum(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val

        return self.leafSum(root.left) + self.leafSum(root.right)