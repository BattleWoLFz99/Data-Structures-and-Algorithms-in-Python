# https://www.lintcode.com/problem/155/solution/16758

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        # 当左子树或右子树为空时，最小深度取决于另一颗子树
        if leftDepth == 0 or rightDepth == 0:
            return leftDepth + rightDepth + 1
            
        return min(leftDepth, rightDepth) + 1