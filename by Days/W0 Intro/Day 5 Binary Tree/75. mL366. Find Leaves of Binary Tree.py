# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        results = []
        self.helper(root, results)
        
        return results
    
    def helper(self, node, results):
        if not node:
            return 0
        
        left_level = self.helper(node.left, results)
        right_level = self.helper(node.right, results)
        curr_level = max(left_level, right_level) + 1
        
        size = len(results)
        if curr_level > size:
            results.append([])
        print(results)
        results[curr_level - 1].append(node.val)
        
        return curr_level