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
        # 无论如何都是要处理空树应该返回的结果
        if root is None:
            return []
            
        # 99% 的题，不用单独处理叶子节点
        # 这里需要单独处理的原因是 root 是 None 的结果，没有办法用于构造 root 是叶子的结果
        if root.left is None and root.right is None:
            # 处理叶子应该返回的结果
            # 如果叶子的返回结果可以通过两个空节点的返回结果得到
            # 就可以省略这一段代码
            return [str(root.val)]

        # 左子树的返回结果 = self.divide_conquer(root.left)
        leftPaths = self.binaryTreePaths(root.left)
        # 右子树的返回结果 = self.divide_conquer(root.left)
    	rightPaths = self.binaryTreePaths(root.right)
        
        # 整棵树的结果 = 按照一定方法合并左右子树的结果
        paths = []
        for path in leftPaths + rightPaths:
            paths.append(str(root.val) + '->' + path)
            
        # return 整棵树的结果
        return paths