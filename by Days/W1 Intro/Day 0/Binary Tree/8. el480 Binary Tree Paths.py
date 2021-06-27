"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if not root:
            return []
        
        paths = []
        self.find_paths(root, [root], paths)
        return paths
    
    def find_paths(self, node, path, paths):
        if not node:
            return
        
        if not node.left and not node.right:
            paths.append('->'.join([str(n.val) for n in path]))
            return
            
        path.append(node.left)
        self.find_paths(node.left, path, paths)
        path.pop()
        
        path.append(node.right)
        self.find_paths(node.right, path, paths)
        path.pop()