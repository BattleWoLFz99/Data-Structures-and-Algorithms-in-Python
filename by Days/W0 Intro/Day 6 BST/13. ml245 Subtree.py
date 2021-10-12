class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        # 空树是非空树的子树:
        if T2 is None:
            return True
        
        # 非空树不是空树的子树：
        if T1 is None:
            return False

        if self.is_equal(T1, T2):
            return True

        # 如果 subtree 是 tree 的左子树或右子树的子树，那么就是 tree 的子树
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

    def is_equal(self, T1, T2):
        if T1 is None and T2 is None:
            return True

        if T1 is None or T2 is None:
            return False

        if T1.val != T2.val:
            return False

        return self.is_equal(T1.left, T2.left) and self.is_equal(T1.right, T2.right)


# 因为很大，递归会炸233  W0 不会管，去看后面吧