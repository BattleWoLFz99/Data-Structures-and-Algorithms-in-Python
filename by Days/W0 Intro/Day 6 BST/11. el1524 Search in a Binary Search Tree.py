class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        if not root:
            return 

        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right

        # 简化了 if root
        return root


class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        if root is None or root.val == val:
            return root
            
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)