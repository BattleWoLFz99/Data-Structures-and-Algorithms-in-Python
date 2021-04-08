# Iterative
def search(lst, value):
    current_node = lst.head_node
    while current_node:
        if current_node.data == value:
            return True
        current_node = current_node.next_element
    return False

# Recursive
def search(node, value):

    if(not node):
        return False

    # check if the node's data matches our value
    if(node.data is value):
        return True  # value found

    # Recursive call to next node in the list
    return search(node.next_element, value)