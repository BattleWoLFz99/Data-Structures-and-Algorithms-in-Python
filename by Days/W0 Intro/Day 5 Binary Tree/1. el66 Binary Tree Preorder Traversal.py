# Version 1: Recursion

""" Definition of TreeNode: 
class TreeNode: 
    def __init__(self, val): 
        this.val = val 
        this.left, this.right = None, None
"""

class Solution:
    """ @param root: The root of binary tree. 
    @return: Preorder in ArrayList which contains node values. 
    """

    def preorderTraversal(self, root):
        if not root:
            return []

        results = []
        self.traverse(root, results)
        return results

    def traverse(self, root, results):
        if root is None:
            return

        results.append(root.val)
        self.traverse(root.left, results)
        self.traverse(root.right, results)

# Shorter:
    def preorderTraversal(self, root):
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + \
        self.preorderTraversal(root.right)


# DFS non-Recursive

    def preorderTraversal(self, root):
        if root is None:
            return []

        stack = [root]
        results = []
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return results