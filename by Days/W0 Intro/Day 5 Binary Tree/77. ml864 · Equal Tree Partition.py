from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def check_equal_tree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        nodes_sum = []
        total_sum = self.get_sum(root, nodes_sum)
        # 要 pop 掉 root 的 sum，也就是最后那个，所以必须用 list
        nodes_sum.pop()
        if total_sum % 2 != 0:
            return False
        for value in nodes_sum:
            if value == total_sum // 2:
                return True
        return False

    def get_sum(self, node, nodes_sum):
        if not node:
            return 0
        if not node.left and not node.right:
            nodes_sum.append(node.val)
            return node.val

        left_sum = self.get_sum(node.left, nodes_sum)
        right_sum = self.get_sum(node.right, nodes_sum)
        curr_sum = left_sum + right_sum + node.val
        nodes_sum.append(curr_sum)

        return curr_sum