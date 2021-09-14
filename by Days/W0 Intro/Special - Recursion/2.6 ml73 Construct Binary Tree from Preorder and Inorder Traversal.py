"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param preorder: A list of integers that preorder traversal of a tree
    @param inorder: A list of integers that inorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        return self.build_tree(preorder, 0, len(preorder) - 1,
                               inorder, 0, len(inorder) - 1)

    def build_tree(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end:
            return None
        if in_start > in_end:
            return None

        root = TreeNode(preorder[pre_start])
        position = inorder.index(preorder[pre_start])

        left_len = position - in_start
        right_len = in_end - position

        root.left = self.build_tree(preorder, pre_start + 1, pre_start + left_len, 
                                    inorder, in_start, position - 1)
        root.right = self.build_tree(preorder, pre_start + left_len + 1, pre_end, 
                                     inorder, position + 1, in_end)

        return root