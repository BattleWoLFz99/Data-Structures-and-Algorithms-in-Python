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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head
        
        # not slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
    
        return False