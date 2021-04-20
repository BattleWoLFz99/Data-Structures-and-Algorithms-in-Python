def find_mid(lst):
    # Write your code here
    length = 0
    curr_node = lst.head_node

    if lst.is_empty():
        return -1

    while curr_node is not None:
        length += 1
        curr_node = curr_node.next_element

    if length % 2 == 0:
        length /= 2
    else:
        length = length/2 + 0.5

    curr_node = lst.head_node
    while length != 1:
        curr_node = curr_node.next_element
        length -= 1

    return curr_node.data


# Better Solution:

def find_mid(lst):
    if lst.is_empty():
        return -1
    current_node = lst.get_head()
    if current_node.next_element is None:
        # Only 1 element exist in array so return its value.
        return current_node.data

    mid_node = current_node
    current_node = current_node.next_element.next_element
    # Move mid_node (Slower) one step at a time
    # Move current_node (Faster) two steps at a time
    # When current_node reaches at end, mid_node will be at the middle of List
    while current_node:
        mid_node = mid_node.next_element
        current_node = current_node.next_element
        if current_node:
            current_node = current_node.next_element
    if mid_node:
        return mid_node.data
    return -1
