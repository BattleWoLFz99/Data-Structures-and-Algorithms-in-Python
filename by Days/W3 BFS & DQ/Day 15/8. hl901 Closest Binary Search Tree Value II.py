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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        lower_stack = self.get_stack(root, target)
        upper_stack = list(lower_stack)
        if lower_stack[-1].val <target:
            self.move_upper(upper_stack)
        else:
            self.move_lower(lower_stack)
            
        results = []
        for _ in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                results.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                results.append(upper_stack[-1].val)
                self.move_upper(upper_stack)

        return results

    def get_stack(self, root, target):
        stack = []
        while root:
            if root.val > target:
                stack.append(root)
                root = root.left
            elif root.val < target:
                stack.append(root)
                root = root.right
            else:
                stack.append(root)
                return root
        
        return stack

    def is_lower_closer(self, lower_stack, upper_stack, target):
        if not lower_stack:
            return False
        if not upper_stack:
            return True
        return abs(lower_stack[-1].val - target) <= abs(upper_stack[-1].val - target)

    def move_lower(self, stack):
        node = stack[-1]
        if node.left:
            n = node.left
            while n:
                stack.append(n)
                n = n.right
        else:
            n = stack.pop()
            while stack and stack[-1].left == n:
                n = stack.pop()

    def move_upper(self, stack):
        node = stack[-1]
        if node.right:
            n = node.right
            while n:
                stack.append(n)
                n = n.left
        else:
            n = stack.pop()
            while stack and stack[-1].right == n:
                n = stack.pop()