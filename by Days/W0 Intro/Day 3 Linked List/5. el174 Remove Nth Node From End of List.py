"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
        
        sentinel = ListNode(0, head)
        fast_node = sentinel
        slow_node = sentinel
        
        while fast_node and n != 0:
            fast_node = fast_node.next
            n -= 1
        
        # Check if the n is bigger than the length of the linked list
        if n != 0:
            return None
        
        while fast_node.next is not None:
            fast_node = fast_node.next
            slow_node = slow_node.next
            
        slow_node.next = slow_node.next.next
        
        return sentinel.next