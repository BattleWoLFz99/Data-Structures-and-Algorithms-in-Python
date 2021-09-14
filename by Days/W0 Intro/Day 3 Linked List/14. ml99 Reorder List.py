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
    @return: nothing
    """
    def reorderList(self, head):
        if not head:
            return None

        mid = self.find_mid(head)
        first_half = head
        second_half = self.reverse(mid.next)
        mid.next = None

        return self.merge(first_half, second_half)

    def find_mid(self, head):
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
        prev = None
        curr = head
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            curr.next = l1
            l1 = l1.next
            curr = curr.next

            curr.next = l2
            l2 = l2.next
            curr = curr.next
        
        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next   

        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

        return dummy.next