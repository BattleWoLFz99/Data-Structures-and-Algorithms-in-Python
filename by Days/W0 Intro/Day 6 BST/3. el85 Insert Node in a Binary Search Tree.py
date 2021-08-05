# 其实这个版本感觉还挺乱的2333
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if root is None:
            return node
            
        curr = root
        while curr != node:
            if node.val < curr.val:
                if curr.left is None:
                    curr.left = node
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                curr = curr.right

        return root


# DQ Ver.
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node

        if node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
            
        return root