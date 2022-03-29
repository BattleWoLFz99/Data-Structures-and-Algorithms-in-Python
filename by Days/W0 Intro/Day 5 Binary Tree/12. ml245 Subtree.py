    def is_subtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.is_equal(root, subRoot):
            return True
        return self.is_subtree(root.left, subRoot) or \
            self.is_subtree(root.right, subRoot)
        
    def is_equal(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1.val != tree2.val:
            return False
        return self.is_equal(tree1.left, tree2.left) and \
            self.is_equal(tree1.right, tree2.right)


# 然后爆栈了：随手就来了个DFS前序非递归
    def is_subtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        stack = [root]
        while stack:
            node = stack.pop()
            if self.is_equal(node, subRoot):
                return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return False