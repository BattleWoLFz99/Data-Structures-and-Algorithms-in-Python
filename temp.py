from typing import List


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


Node1 = ListNode(1)
Node1.next = ListNode(2)

v1_prev = ListNode(None, Node1)
v1_node = Node1
v1_node.next = None

v2_prev = ListNode(None, Node1)
v2_node = Node1
v2_node.next = None

v1_prev.next = v2_node
v2_prev.next = v1_node
v1_node.next, v2_node.next = v2_node.next, v1_node.next

print(v1_node.val)
print(v2_node.val)