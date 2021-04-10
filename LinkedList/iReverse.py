def reverse(lst):
    # Write your code here
    prev = None
    curr = lst.head_node
    next = None

    while curr:
        next = curr.next_element
        curr.next_element = prev
        prev = curr
        curr = next
        # remember the head_node
        lst.head_node = prev
    return lst
