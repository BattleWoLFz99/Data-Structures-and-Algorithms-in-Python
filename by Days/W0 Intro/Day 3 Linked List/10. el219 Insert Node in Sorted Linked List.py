"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        sentinel = ListNode(0, head)
        curr_node = sentinel

        while curr_node.next and curr_node.next.val < val:
            curr_node = curr_node.next
        
        node = ListNode(val, curr_node.next)
        curr_node.next = node

        return sentinel.next