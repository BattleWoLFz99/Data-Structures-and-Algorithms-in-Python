class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trimBST(self, root, minimum, maximum):
        if root is None:
            return None

        if minimum <= root.val and root.val <= maximum:
            root.left = self.trimBST(root.left, minimum, maximum)
            root.right = self.trimBST(root.right, minimum, maximum)
            return root
        # BST, 当前都小于了，左边不需要看了，直接判断上面的 left 接下面的 right
        elif root.val < minimum:
            return self.trimBST(root.right, minimum, maximum)
        else:
            return self.trimBST(root.left, minimum, maximum)


# 夏天版（提升逻辑复杂度的）：
class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trimBST(self, root, minimum, maximum):
        if root is None:
            return None

        root_val = root.val
        if minimum <= root_val and root_val <= maximum:
            root.left = self.trimBST(root.left, minimum, root_val)
            root.right = self.trimBST(root.right, root_val, maximum)
            return root
        # BST, 当前都小于了，左边不需要看了，直接判断上面的 left 接下面的 right
        elif root_val < minimum:
            return self.trimBST(root.right, minimum, maximum)
        else:
            return self.trimBST(root.left, minimum, maximum)