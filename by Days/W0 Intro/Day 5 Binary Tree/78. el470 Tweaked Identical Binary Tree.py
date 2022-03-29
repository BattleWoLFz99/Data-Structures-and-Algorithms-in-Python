class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are tweaked identical, or false.
    """
    def is_tweaked_identical(self, a: TreeNode, b: TreeNode) -> bool:
        return self.dfs(a, b)

    def dfs(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return(False)
        if a.val != b.val:
            return(False)

        no_invert = self.dfs(a.left, b.left) and self.dfs(a.right, b.right)
        invert = self.dfs(a.left, b.right) and self.dfs(a.right, b.left)
        return no_invert or invert