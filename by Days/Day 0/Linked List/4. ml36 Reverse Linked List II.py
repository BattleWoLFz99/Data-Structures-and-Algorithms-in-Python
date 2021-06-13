"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        sentinel = ListNode(-1, head)
        mth_prev = self.findkth(sentinel, m - 1)
        mth = mth_prev.next
        nth = self.findkth(sentinel, n)
        nth_next = nth.next
        nth.next = None

        self.reverse(mth)
        mth_prev.next = nth
        mth.next = nth_next
        return sentinel.next

    def reverse(self, head):
        prev = None
        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def findkth(self, head, k):
        for i in range(k):
            if head is None:
                return None
            head = head.next
        return head