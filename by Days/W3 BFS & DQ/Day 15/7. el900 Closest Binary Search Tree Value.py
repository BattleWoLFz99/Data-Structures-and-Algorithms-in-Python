# Ver 1:
#  Not really great non-recursion Ver.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if not root:
            return []

        stack = []
        results = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        start, end = 0, len(results) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if results[mid] < target:
                start = mid
            else:
                end = mid

        if target - results[start] < results[end] - target:
            return results[start]
        else:
            return results[end]


#  Why do I even copy this.... No need to look at it
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if not root:
            return []

        results = self.traverse(root)

        start, end = 0, len(results) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if results[mid] < target:
                start = mid
            else:
                end = mid

        if target - results[start] < results[end] - target:
            return results[start]
        else:
            return results[end]


    def traverse(self, root):
        if not root:
            return []

        return self.traverse(root.left) + [root.val] + self.traverse(root.right)




# DQ

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if root is None:
            return None
            
        lower = self.get_lower_bound(root, target)
        upper = self.get_upper_bound(root, target)
        
        if lower is None:
            return upper.val
        if upper is None:
            return lower.val
            
        if target - lower.val < upper.val - target:
            return lower.val
        return upper.val
        
    def get_lower_bound(self, root, target):
        # get the largest node that < target
        if root is None:
            return None
        
        if target < root.val:
            return self.get_lower_bound(root.left, target)
            
        lower = self.get_lower_bound(root.right, target)
        return root if lower is None else lower
        
    def get_upper_bound(self, root, target):
        # get the smallest node that >= target
        if root is None:
            return None
        
        if target >= root.val:
            return self.get_upper_bound(root.right, target)
            
        upper = self.get_upper_bound(root.left, target)
        return root if upper is None else upper



# non-recursion(iteration):
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if root is None:
            return None
            
        lower = root
        upper = root

        while root:
            if root.val < target:
                lower = root
                root = root.right
            elif root.val > target:
                upper = root
                root = root.left
            else:
                return root.val

        if abs(target - lower.val) < abs(upper.val - target):
            return lower.val
        else:
            return upper.val



# non-recurstion ver.

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if root is None:
            return None
            
        lower = root
        upper = root

        while root:
            if root.val < target:
                lower = root
                root = root.right
            elif root.val > target:
                upper = root
                root = root.left
            else:
                return root.val

        if abs(target - lower.val) < abs(upper.val - target):
            return lower.val
        else:
            return upper.val