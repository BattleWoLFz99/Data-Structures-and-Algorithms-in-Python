# Must have "is not None"
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        is_BST, _, _ = self.helper(root)
        
        return is_BST
        
    def helper(self, root):
        if root is None:
            return True, None, None
        
        left_is_BST, left_min, left_max = self.helper(root.left)
        right_is_BST, right_min, right_max = self.helper(root.right)
        
        if not left_is_BST or not right_is_BST:
            return False, None, None
        if left_max is not None and left_max >= root.val:
            return False, None, None
        if right_min is not None and right_min <= root.val:
            return False, None, None
        
        # is BST
        min_node_val = left_min if left_min is not None else root.val
        max_node_val = right_max if right_max is not None else root.val
        
        return True, min_node_val, max_node_val