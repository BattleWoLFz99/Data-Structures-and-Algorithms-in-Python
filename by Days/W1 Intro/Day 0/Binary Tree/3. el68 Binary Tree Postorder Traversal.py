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



# Shorter:
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        return self.postorder(root)
    
    def postorder(self, root):
        if not root:
            return []

        return self.postorder(root.left) + self.postorder(root.right) + [root.val]



# Shorter:
    def postorderTraversal(self, root):
        if not root:
            return []

        return self.postorderTraversal(root.left) + \
        self.postorderTraversal(root.right) + [root.val]



# 1. 一样能往left走就先往left走
# 2. 若一个node:
#   没有right，输出
#   有right，由于post-order是right走过了才能输出当前node，所以我们需要多纪录前一个node是谁
#       前一个node是从right来的，right已经走过，输出
#       right还没走过，把right和它所有的left加到stack，这轮不输出(continue)
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