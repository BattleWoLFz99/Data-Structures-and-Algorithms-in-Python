"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head: the head of linked list.
    # @param val: an integer
    # @return: a linked node or null
    def findNode(self, head, val):
        # Write your code here
        while head:
            if head.val == val:
                return head
            head = head.next
        return None