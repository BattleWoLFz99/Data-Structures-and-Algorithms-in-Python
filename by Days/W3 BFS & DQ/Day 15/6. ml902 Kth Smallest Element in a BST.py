# Traverse requires O(n) space do not use
# 事实证明一刷刷了个P系列以及精刷的重要性

# non-recursion Shorter Ver.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        for _ in range(k - 1):
            node = stack[-1]
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
                    
        return stack[-1].val


# non-Recursion Shorter Ver.
    def kthSmallest(self, root, k):
        if not root:
            return None

        stack = []
        while root:
            stack.append(root)
            root = root.left

        for _ in range(k-1):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return stack[-1].val