# 递归的三要素：
#	 1. 递归的定义
#	 3. 递归的出口(空)
#    2. 递归的拆解


# 二叉树的所有路径 遍历法 + 回溯:

# Not recommended, easier to understand:
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
            
        result = []
        self.dfs(root, [], result)
        return result

    def dfs(self, node, path, result):
        path.append(str(node.val))
        
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            path.pop()
            return

        if node.left:
            self.dfs(node.left, path, result)
        
        if node.right:
            self.dfs(node.right, path, result)

        path.pop()


# 再演变为：
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




# --------------------------

# 使用 Divider Conquer 版本的 DFS
# 利用 return value 记录子问题结果

# easier to understand:
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        paths = []
        # 无论如何都是要处理空树应该返回的结果
        if not root:
            return paths

        # 90% 的题，不用单独处理叶子节点
        # 只要保证到下面两个空的结果合并出来到整个树的结果是对的，就不需要单独处理叶子节点
        # 这里需要单独处理的原因是 root 是 None 的结果，没有办法用于构造 root 是叶子的结果
        # 需要单独考虑一个叶子节点，那么没有 ->
        if not root.left and not root.right:
            # 处理叶子应该返回的结果
            # 如果叶子的返回结果可以通过两个空节点的返回结果得到
            # 就可以省略这一段代码
            return[str(root.val)]

        # 左子树的返回结果 = self.divide_conquer(root.left)
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + "->" + path)
        # 右子树的返回结果 = self.divide_conquer(root.left)
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + "->" + path)

        # return 整棵树的结果
        return paths


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
            
        # 90% 的题，不用单独处理叶子节点
        # 这里需要单独处理的原因是 root 是 None 的结果，没有办法用于构造 root 是叶子的结果
        # 需要单独考虑一个叶子节点，那么没有 ->
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