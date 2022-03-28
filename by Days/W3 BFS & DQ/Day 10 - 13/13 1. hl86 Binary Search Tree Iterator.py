# 不仅仅是BST，任何二叉树都能这样中序遍历。建立在理解基础上背下来是最好的
# 通用解法。 可以同时用于 find k values in the BST that are closest to the target.

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return bool(self.stack)

    """
    @return: return next node
    """
    def _next(self):
        node = self.stack[-1]
        if node.right:
            n = node.right
            while n:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        
        return node