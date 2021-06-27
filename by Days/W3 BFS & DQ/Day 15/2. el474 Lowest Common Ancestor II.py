"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        parents = set()
        curr = A
        while curr:
            parents.add(curr)
            curr = curr.parent

        curr = B
        while curr:
            if curr in parents:
                return curr
            curr = curr.parent

        return None