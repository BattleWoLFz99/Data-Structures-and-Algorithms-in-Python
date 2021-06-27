# Below is a bad solution:
    # DO NOT USE global variables like this
    # DIRECTIONS is accepeted.
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """


    def findSubtree(self, root):
        self.minimum_weight = float('inf')
        self.minimum_subtree_root = None
        self.getTreeSum(root)

        return self.minimum_subtree_root

    def getTreeSum(self, root):
        if root is None:
            return 0

        left_weight = self.getTreeSum(root.left)
        right_weight = self.getTreeSum(root.right)
        root_weight = left_weight + right_weight + root.val
        
        if root_weight < self.minimum_weight:
            self.minimum_weight = root_weight
            self.minimum_subtree_root = root

        return root_weight



# No Global Variables ver.
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """


    def findSubtree(self, root):
        minimum, subtree, sum_of_root = self.get_min_tree_sum(root)
        return subtree

    def get_min_tree_sum(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_minimum, left_subtree, left_sum = self.get_min_tree_sum(root.left)
        right_minimum, right_subtree, right_sum = self.get_min_tree_sum(root.right)

        sum_of_root = left_sum + right_sum + root.val

        if left_minimum == min(left_minimum, right_minimum, sum_of_root):
            return left_minimum, left_subtree, sum_of_root

        if right_minimum == min(left_minimum, right_minimum, sum_of_root):
            return right_minimum, right_subtree, sum_of_root       

        return sum_of_root, root, sum_of_root