# Add more limitation, then consider removing.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        sentinel = ListNode(0, head)
        
        curr_node = sentinel.next
        prev_node = sentinel
        
        while curr_node:
            if curr_node.next and curr_node.val == curr_node.next.val:
                while curr_node.next and curr_node.val == curr_node.next.val:
                    curr_node.next = curr_node.next.next
                prev_node.next = curr_node.next
            else:
                prev_node = prev_node.next
            curr_node = curr_node.next

        return sentinel.next