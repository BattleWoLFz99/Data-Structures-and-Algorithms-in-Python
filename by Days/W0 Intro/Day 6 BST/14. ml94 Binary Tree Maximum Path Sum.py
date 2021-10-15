class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
        self.max_sum = float('-inf')
        
    def maxPathSum(self, root):
        # write your code here
        if root is None:
            return 0

        self.get_max_path_sum(root)
        return self.max_sum

    def get_max_path_sum(self, root):
        if root is None:
            return 0

        max_left = self.get_max_path_sum(root.left)
        max_right = self.get_max_path_sum(root.right)

        self.max_sum = max(self.max_sum, max_left + max_right + root.val)
        curr_max = root.val + max(max_left, max_right)

        return curr_max if curr_max > 0 else 0