"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        nums = []
        cur = None
    
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                
                if cur.right == root:
                    nums.append(root.val)
                    cur.right = None
                    root = root.right
                else:
                    cur.right = root
                    root = root.left
            else:
                nums.append(root.val)
                root = root.right
                
        return nums