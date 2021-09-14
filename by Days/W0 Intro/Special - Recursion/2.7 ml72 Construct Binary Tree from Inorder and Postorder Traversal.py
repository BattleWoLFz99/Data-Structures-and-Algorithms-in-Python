"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        return self.build_tree(inorder, 0, len(inorder) - 1,
                               postorder, 0, len(postorder) - 1)
    
    def build_tree(self, inorder, in_start, in_end, postorder, post_start, post_end):
        if in_start > in_end:
            return None
        if post_start > post_end:
            return None

        root = TreeNode(postorder[post_end])
        position = inorder.index(postorder[post_end])

        left_len = position - in_start
        right_len = in_end - position

        root.left = self.build_tree(inorder, in_start, position - 1, 
                                    postorder, post_start, post_start + left_len - 1)
        root.right = self.build_tree(inorder, position + 1, in_end, 
                                     postorder, post_end - right_len, post_end - 1)

        return root