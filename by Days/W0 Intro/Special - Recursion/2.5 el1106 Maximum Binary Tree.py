"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        return self.build_tree(nums, 0 , len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start > end:
            return None

        max_number = max(nums[start:end + 1])
        position = nums.index(max_number)
        
        root = TreeNode(max_number)
        root.left = self.build_tree(nums, start, position - 1)
        root.right = self.build_tree(nums, position + 1, end)

        return root
