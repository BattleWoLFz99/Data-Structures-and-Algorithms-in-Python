# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        
        dummy_node = ListNode(0)
        dummy_node.next = head
        fast_node = dummy_node
        slow_node = dummy_node
        
        while (fast_node is not None) and (n != 0):
            fast_node = fast_node.next
            n -= 1
        
        # Check if the n is bigger than the length of the linked list
        if n != 0:
            return None
        
        while fast_node.next is not None:
            fast_node = fast_node.next
            slow_node = slow_node.next
            
        slow_node.next = slow_node.next.next
        
        return dummy_node.next