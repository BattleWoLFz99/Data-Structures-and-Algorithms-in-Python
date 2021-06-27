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
        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


# Shorter:
    def preorderTraversal(self, root):
        return self.pre(root)
    
    def pre(self, root):
        if not root:
            return []

        return [root.val] + self.pre(root.left) + self.pre(root.right)



# DFS

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in list which contains node values.
    """
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return preorder


# DQ

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in list which contains node values.
    """
    def preorderTraversal(self, root):
        res = []
        if root is None:
            return []
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        res.append(root.val)
        if left:
            res.extend(left)
        if right:
            res.extend(right)
        return res