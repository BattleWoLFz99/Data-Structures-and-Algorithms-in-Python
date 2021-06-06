# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        curr_node = dummy_node
        while l1 and l2:
            if l1.val < l2.val:
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next
        if l1:
            curr_node.next = l1
        if l2:
            curr_node.next = l2
        return dummy_node.next