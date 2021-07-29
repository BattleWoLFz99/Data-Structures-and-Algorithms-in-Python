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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None or head.next is None:
            return None

        slow = fast = head  		#初始化快指针和慢指针
        while fast and fast.next:	
            slow = slow.next
            fast = fast.next.next
            if fast == slow:		#快慢指针相遇
                break

        if slow == fast:
            slow = head				#从头移动慢指针
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow				#两指针相遇处即为环的入口
            
        return None