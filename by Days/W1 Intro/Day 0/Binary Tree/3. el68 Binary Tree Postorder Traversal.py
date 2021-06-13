# Version 0: Recursion

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        self.results.append(root.val)




#Version 1: Non-Recursion
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if not root:
            return []

        ans = []
        stack = []
        while root:
            stack.append(root)
            root = root.left

        prev_node = None
        while stack:
            node = stack[-1]
            if node.right and prev_node != node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
                continue
            node = stack.pop()
            ans.append(node.val)
            prev_node = node
        return ans