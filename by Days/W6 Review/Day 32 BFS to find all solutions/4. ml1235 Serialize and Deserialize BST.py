"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def serialize(self, root):
        # write your code here
        if not root:
            return '{}'
            
        p = [root]
        result = [root.val]
        while p:
            new_p = []
            for n in p:
                if n.left:
                    new_p.append(n.left)
                    result.extend([n.left.val])
                else:
                    result.extend('#')
                    
                if n.right:
                    new_p.append(n.right)
                    result.extend([n.right.val])
                else:
                    result.extend('#')

            p = new_p
        
        while result and result[-1] == '#':
            result.pop()
     
        return '{' + ','.join(map(str, result)) + '}' 

    def deserialize(self, data):
        if data == '{}':
            return 
        
        nodes = collections.deque([TreeNode(n) for n in data[1:-1].split(',')])
        root = nodes.popleft()
        p = [root]
        while p:
            new_p = []
            for n in p:
                if nodes:
                    left_node = nodes.popleft()
                    if left_node.val != '#':
                        n.left = left_node
                        new_p.append(n.left)
                    else:
                        n.left = None
                    

                if nodes:
                    right_node = nodes.popleft()
                    if right_node.val != '#':
                        n.right = right_node
                        new_p.append(n.right)
                    else:
                        n.right = None
                    
            p = new_p  

        return root