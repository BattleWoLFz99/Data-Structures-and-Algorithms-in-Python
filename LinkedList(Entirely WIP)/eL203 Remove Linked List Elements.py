# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        curr_node = dummy_head
        while curr_node.next is not None:
            if curr_node.next.val is val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
                
        return dummy_head.next