"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return the head of new linked list
    def insertNode(self, head, val):
        # Write your code here
        dummy = ListNode(0, head)
        p = dummy
        while p.next and p.next.val < val:
            p = p.next
        node = ListNode(val, p.next)
        p.next = node
        return dummy.next