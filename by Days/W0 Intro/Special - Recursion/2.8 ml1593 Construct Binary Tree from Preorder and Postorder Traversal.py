"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def constructFromPrePost(self, pre, post):
        return self.build_tree(pre, 0, len(pre) - 1, post, 0, len(post) - 1)

    def build_tree(self, pre, pre_start, pre_end, post, post_start, post_end):
        if pre_start > pre_end:
            return None
        if post_start > post_end:
            return None
        
        if pre[pre_start] != post[post_end]:
            return None

        root = TreeNode(pre[pre_start])

        if pre_start == pre_end or post_start == post_end:
            return root
        
        position = post.index(pre[pre_start + 1])
        left_len = position - post_start + 1
        right_len = post_end - position - 1

        root.left = self.build_tree(pre, pre_start + 1, pre_start + left_len,
                                    post, post_start, post_start + left_len - 1)
        root.right = self.build_tree(pre, pre_end - right_len + 1, pre_end,
                                    post, post_end - right_len, post_end - 1)

        return root