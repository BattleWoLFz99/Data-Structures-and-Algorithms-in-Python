# 使用 Divider Conquer 版本的 DFS

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
        if root is None:
            return []
            
        # 99% 的题，不用单独处理叶子节点
        # 这里需要单独处理的原因是 root 是 None 的结果，没有办法用于构造 root 是叶子的结果
        if root.left is None and root.right is None:
            return [str(root.val)]

        leftPaths = self.binaryTreePaths(root.left)
    	rightPaths = self.binaryTreePaths(root.right)
        
        paths = []
        for path in leftPaths + rightPaths:
            paths.append(str(root.val) + '->' + path)
            
        return paths