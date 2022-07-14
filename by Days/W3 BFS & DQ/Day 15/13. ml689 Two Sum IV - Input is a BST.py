"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        if not root:
            return None

        lower_stack = self.get_min_value_path(root)
        upper_stack = self.get_max_value_path(root)

        results = []
        while lower_stack[-1] != upper_stack[-1]:
            if lower_stack[-1].val + upper_stack[-1].val > n:
                self.move_upper(upper_stack)
            elif lower_stack[-1].val + upper_stack[-1].val < n:
                self.move_lower(lower_stack)
            else:
                return ([lower_stack[-1].val, upper_stack[-1].val])
        
        return []

    def get_min_value_path(self, root):
        stack = []
        while root:
            stack.append(root)
            root = root.left

        return stack

    def get_max_value_path(self, root):
        stack = []
        while root:
            stack.append(root)
            root = root.right

        return stack

    def move_upper(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()

    def move_lower(self, stack):
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
