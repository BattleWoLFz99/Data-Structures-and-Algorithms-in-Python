# This solution is just damn slow that only beats 5% because it is originally designed for non-sorted linked list without returning in sorted order.
# This solution was for https://www.educative.io/courses/data-structures-coding-interviews-python/qVV2BA033M0, We can write a more efficient solution using hashing.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        if head.next is None:
            return head
        curr_node = dummy_node
        rest_node = curr_node.next
        while curr_node.next:
            key = curr_node.next.val
            while rest_node.next:
                if rest_node.next.val == key:
                    rest_node.next = rest_node.next.next
                else:
                    rest_node = rest_node.next
            curr_node = curr_node.next
            rest_node = curr_node.next

        return dummy_node.next
        