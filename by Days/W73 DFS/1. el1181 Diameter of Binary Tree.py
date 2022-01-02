"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        _, max_diameter = self.dfs(root)
        return max_diameter

    def dfs(self, root):
        if not root:
            return 0, 0

        left_longest, left_max_diameter = self.dfs(root.left)
        right_longest, right_max_diameter = self.dfs(root.right)

        curr_height = max(left_longest, right_longest) + 1
        curr_max_diameter = max(
            left_max_diameter,
            right_max_diameter,
            left_longest + right_longest
        )

        return curr_height, curr_max_diameter
