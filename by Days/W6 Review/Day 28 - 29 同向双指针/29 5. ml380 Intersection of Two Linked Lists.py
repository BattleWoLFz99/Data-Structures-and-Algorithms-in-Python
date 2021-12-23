"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        
        if not headA or not headA.next or not headB:
            return None 
            
        tailA = headA
        while tailA.next:
            tailA = tailA.next
            
        tailA.next = headB
        
        slow, fast = headA, headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow is fast:
                break
            
        if slow is fast:
            slow = headA 
            while slow is not fast:
                slow = slow.next
                fast = fast.next 
            tailA.next = None
            return slow
        
        tailA.next = None
        return None


# Without modifying:
class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0
        node1, node2 = headA, headB
        while node1 is not None:
            lenA += 1
            node1 = node1.next
        while node2 is not None:
            lenB += 1
            node2 = node2.next
        
        node1, node2 = headA, headB
        while lenA > lenB:
            node1 = node1.next
            lenA -= 1
        while lenB > lenA:
            node2 = node2.next
            lenB -=1
        while node1 is not node2:
            node1 = node1.next
            node2 = node2.next
        return node1