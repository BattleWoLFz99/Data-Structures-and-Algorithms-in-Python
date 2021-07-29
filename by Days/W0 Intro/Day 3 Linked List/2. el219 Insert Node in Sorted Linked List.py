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
        sentinel = ListNode(-1, head)
        curr = sentinel
        while curr.next and curr.next.val < val:
            curr = curr.next

        node = ListNode(val, curr.next)
        curr.next = node

        return sentinel.next

