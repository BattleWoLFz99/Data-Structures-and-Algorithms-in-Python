    def tree2str(self, t: TreeNode) -> str:
        # 怎么起手 BFS 的，BFS怎么做先序遍历？？
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        if not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + \
            self.tree2str(t.right) + ")"