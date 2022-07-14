class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.children = []
        self.is_deleted = False

    def traverse(self, root):
        result = []
        self.traverse_helper(root, result)
        return result

    def traverse_helper(self, root, result):
        if not root.is_deleted:
            result.append(root.val)
        for child in root.children:
            self.traverse_helper(child, result)
    """
    @param root: the node where added
    @param value: the added node's value
    @return: add a node, return the node
    """
    def addNode(self, root, value):
        new_node = MyTreeNode(value)
        new_node.parent = root
        root.children.append(new_node)
        return new_node
    """
    @param root: the deleted node
    @return: nothing
    """
    def deleteNode(self, root):
        root.is_deleted = True
        return