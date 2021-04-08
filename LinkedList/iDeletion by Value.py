# Deletion needs previous_node
def delete(lst, value):
    deleted = False
    if lst.head_node is None:
        print("List is Empty")
        return deleted
    current_node = lst.head_node
    previous_node = None
    if current_node.data is value: #head deletion
        current_node.head_node = current_node.next_element
        current_node.next_element = None
        deleted = True
        return deleted

    # Traversing/Searching for Node to Delete
    while current_node:
        # Node to delete is found
        if value == current_node.data:
            # previous node now points to next node
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            # current_node.next_element = current_node.next_element.next_element may AttributeError: 'NoneType' object has no attribute 'next_element'
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element

    if deleted is False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")

    return deleted