# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ncpc, hh

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        
        return head