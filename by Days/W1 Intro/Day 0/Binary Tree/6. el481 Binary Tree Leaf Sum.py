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
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val

        return self.leafSum(root.left) + self.leafSum(root.right)