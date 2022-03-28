# 习惯后直接全扔 return 里
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        return self.helper(root, [root.val], paths, targetSum)
    
    def helper(self, node, targetSum):
        if not node:
            return False
        if not node.left and not node.right and node.val == targetSum:
            return True
        
        left = self.helper(node.left, targetSum - node.val)
        right = self.helper(node.left, targetSum - node.val)
        
        return left or right
        

# DFS with stack
def hasPathSum2(self, root, sum):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == sum:
            return True
        if curr.right:
            stack.append((curr.right, val + curr.right.val))
        if curr.left:
            stack.append((curr.left, val + curr.left.val))
    return False
    
# BFS with queue
def hasPathSum(self, root, sum):
    if not root:
        return False
    queue = [(root, sum-root.val)]
    while queue:
        curr, val = queue.pop(0)
        if not curr.left and not curr.right and val == 0:
            return True
        if curr.left:
            queue.append((curr.left, val - curr.left.val))
        if curr.right:
            queue.append((curr.right, val - curr.right.val))
    return False
	
def hasPathSum1(self, root, sum):
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)