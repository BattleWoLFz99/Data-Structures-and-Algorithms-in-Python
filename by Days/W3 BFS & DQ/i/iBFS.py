# BFS最好不要用递归，很容易栈溢出

# el69 Binary Tree Level Order Traversal
# Single queue

from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if root is None:
            return []
            
        queue = collections.deque([root])
        results = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)
        return results


# Two queue:
skipped for now

# Dummy Node:
skipped for now