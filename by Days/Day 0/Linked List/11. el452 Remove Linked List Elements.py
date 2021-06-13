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
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        sentinel = ListNode(0, head)
        curr_node = sentinel

        while curr_node.next:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return sentinel.next