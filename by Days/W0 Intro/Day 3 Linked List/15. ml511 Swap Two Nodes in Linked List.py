"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        if not head:
            return None

        dummy = ListNode(-1, head)
        curr = dummy
        v1_node, v2_node = None, None
        while curr.next:
            if curr.next.val == v1:
                v1_prev = curr
                v1_node = curr.next
                v1_next = curr.next.next
            if curr.next.val == v2:
                v2_prev = curr
                v2_node = curr.next
                v2_next = curr.next.next
            curr = curr.next

        if v1_node and v2_node:
            v1_prev.next = v2_node
            v2_prev.next = v1_node
            v1_node.next, v2_node.next = v2_node.next, v1_node.next

        return dummy.next