# Version 0: Recursion
# self.results, return self.results

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
        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.results.append(root.val)
        self.traverse(root.right)


# Shorter:

    def inorderTraversal(self, root):
        # write your code here
        return self.inorder(root)
    
    def inorder(self, root):
        if not root:
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)



#  通用的，能解决大部分题，来自于ml902，然而回不去了
#  先stack.append(root)一路到最左
#  DFS. 
#  如果当前点存在右子树，那么就是右子树中“一路向西”最左边的那个点
#  如果当前点不存在右子树，则是走到当前点的路径中，第一个左拐的点
#  node之后全是node，标准DFS (BFS也是)

    def inorderTraversal(self, root):
        if not root:
            return None

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

        return results



#  注意这里 [-1] 没有pop，带 else 可实现反向遍历(真要只选一个用怕不是是这个)
#  删掉 101 102 (else 里的 while) TLE (因为 append pop 死循环了 while 逻辑一致)

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        stack = []
        result = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack[-1]
            result.append(node.val)
            if node.right: 
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
        return result




# 我也不知道这是个啥，先屯着吧草。

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        ans = []
        stack = []
        curr = root
        while curr or stack:
            if not curr:
                curr = stack.pop(-1)
                ans.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left
        return ans