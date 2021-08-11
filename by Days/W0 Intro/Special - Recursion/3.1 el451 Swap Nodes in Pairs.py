# 递归
class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        first, second = head, head.next
        suffix = self.swapPairs(second.next)

        second.next = first
        first.next = suffix
        return second
        
# 迭代
    def swapPairs(self, head):
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        while curr.next is not None and curr.next.next is not None:
            first, second = curr.next, curr.next.next
            curr.next = second
            first.next = second.next
            second.next = first
            # move to next pair
            curr = first

        return dummy.next