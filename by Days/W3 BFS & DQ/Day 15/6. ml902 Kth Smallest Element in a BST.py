# Recursion Ver.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        if root is None:
            return None

        self.results = []
        self.traverse(root)

        return self.results[k-1]

    def traverse(self, root):
        if not root:
            return []

        self.traverse(root.left)
        self.results.append(root.val)
        self.traverse(root.right)

        return 



# Shorter: (see ml66)
    def kthSmallest(self, root, k):
        if not root:
            return None

        results = self.traverse(root)

        return results[k-1]

    def traverse(self, root):
        if not root:
            return []

        return self.traverse(root.left) + [root.val] + self.traverse(root.right)




# non-recursion Ver.
# Standard el67 inorder

    def kthSmallest(self, root, k):
        if not root:
            return None

        stack = []
        results = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return results[k-1]



# Improved Ver. maybe as follow-up?
    def kthSmallest(self, root, k):
        if not root:
            return None

        stack = []
        results = []

        while root:
            stack.append(root)
            root = root.left

        for _ in range(k-1):
            node = stack.pop()
            results.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return stack[-1].val



# 更通用

