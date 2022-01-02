# 看上去更标准且偷懒省略了 {} 的做法
class Solution:
    def serialize(self, root):
        if root is None:
            return ""
            
        queue = collections.deque([root])
        bfs_order = []
        
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else "#")
            if node:
                queue.append(node.left)
                queue.append(node.right)
                
        return ','.join(bfs_order)

    def deserialize(self, data):
        if not data:
            return None
        
        vals = data.split(',')
        root = TreeNode(int(vals[0])) 
        queue = [root]   # 二叉树的原型
        isLeftChild = True
        index = 0
        
        for val in vals[1:]:   # 第一位已经交给root了
            if val is not "#":
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else: 
                    queue[index].right = node
                queue.append(node)
            
            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild
            
        return root


# 快慢：
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if root is None:
            return ""
            
        # use bfs to serialize the tree
        queue = collections.deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
            
        return ' '.join(bfs_order)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # None or ""
        if not data:
            return None

        bfs_order = [
            TreeNode(int(val)) if val != '#' else None
            for val in data.split()
        ]
        root = bfs_order[0]
        fast_index = 1
        
        nodes, slow_index = [root], 0
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        
        return root