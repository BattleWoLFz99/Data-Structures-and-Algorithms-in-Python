"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if head == None:
            return head

        curr_node = head
        size = 0
        while curr_node != None:
            size += 1
            curr_node = curr_node.next

        k = k % size
        if k == 0:
            return head

        curr_node = head
        for _ in range(size-k-1):
            curr_node = curr_node.next

        new_head = curr_node.next
        curr_node.next = None
        curr_node = new_head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = head
        return new_head


# make it a Circular Linked List:

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if head is None:
            return head
        lock = head
        length = 1
        while lock.next is not None:
            lock = lock.next
            length += 1

        lock.next = head
        k = k % length
        for step in range(length-k):
            lock = lock.next

        head = lock.next
        lock.next = None

        return head