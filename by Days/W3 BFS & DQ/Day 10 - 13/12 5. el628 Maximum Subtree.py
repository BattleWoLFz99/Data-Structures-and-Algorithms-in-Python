"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    maximum_weight = float('-inf')
    result = None

    def findSubtree(self, root):
        # Write your code here
        self.helper(root)

        return self.result

    def helper(self, root):
        if root is None:
            return 0

        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        
        if left_weight + right_weight + root.val >= self.maximum_weight or self.result is None:
            self.maximum_weight = left_weight + right_weight + root.val
            self.result = root

        return left_weight + right_weight + root.val


# 无全局变量
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        if root is None:
            return None

        curr_sum, max_sum, max_subtree = self.get_sum(root)

        return max_subtree
    
    # 分别返回当前子树和，子树中最小的和，目标节点
    def get_sum(self, root):
        if root is None:
            return 0, float('-inf'), None

        left_sum, left_max_sum, left_max_subtree = self.get_sum(root.left)
        right_sum, right_max_sum, right_max_subtree = self.get_sum(root.right)
        curr_sum = root.val + left_sum + right_sum

        max_sum = max(left_max_sum, right_max_sum, curr_sum)
        if curr_sum == max_sum:
            return curr_sum, max_sum, root
        if left_max_sum == max_sum:
            return curr_sum, max_sum, left_max_subtree
        return curr_sum, max_sum, right_max_subtree