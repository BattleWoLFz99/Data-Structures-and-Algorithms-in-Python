# Based on ml88 Ver, a_exist b_exist:
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """ 
    def lowestCommonAncestor3(self, root, A, B):
        if not root:
            return None

        a_exist = False
        b_exist = False

        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == A:
                    a_exist = True
                if node == B:
                    b_exist = True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        if a_exist and b_exist:
            return self.lowestCommonAncestor(root, A, B)
        return None



    def lowestCommonAncestor(self, root, A, B):
        if root is None:
            return None
        if root == A or root == B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right

        return None


# Or better(won't be follow-up)
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """ 
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None
            
        left_a, left_b, left_node = self.helper(root.left, A, B)
        right_a, right_b, right_node = self.helper(root.right, A, B)
        
        a = left_a or right_a or root == A
        b = left_b or right_b or root == B
        
        if root == A or root == B:
            return a, b, root

        if left_node and right_node:
            return a, b, root
        if left_node:
            return a, b, left_node
        if right_node:
            return a, b, right_node

        return a, b, None