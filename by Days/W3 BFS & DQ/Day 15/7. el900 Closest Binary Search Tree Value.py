# 惨不忍睹啊！！！！卧槽一刷刷了个寂寞？
# 树traverse后跟一个二分，哪个神仙教的？！！站出来我保证往死里打！！！！

# 标准分治
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return None
            
        lower = self.get_lower_bound(root, target)
        upper = self.get_upper_bound(root, target)
        
        if lower is None:
            return upper.val
        if upper is None:
            return lower.val
            
        if abs(target - lower.val) < abs(target - upper.val):
            return lower.val
        return upper.val
        
    def get_lower_bound(self, root, target):
        # BST，越往下符合就是越接近
        if root is None:
            return None
        
        if target < root.val:
            return self.get_lower_bound(root.left, target)

        # return 需要 return 的东西    
        lower = self.get_lower_bound(root.right, target)

        return root if lower is None else lower
        
    def get_upper_bound(self, root, target):
        if root is None:
            return None
        
        if target >= root.val:
            return self.get_upper_bound(root.right, target)
        
        upper = self.get_upper_bound(root.left, target)

        return root if upper is None else upper



# non-recursion
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return None
        
        lower = root
        upper = root
        
        while root:
            if root.val < target:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
            
        is_upper_closer = abs(upper.val - target) < abs(target - lower.val)
        return upper.val if is_upper_closer else lower.val


# 删掉后还是捞回来了，挂后面纪念，欣赏下这位一刷时的旷世神作xswl：
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