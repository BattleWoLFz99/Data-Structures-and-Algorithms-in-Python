def length(lst):
    curr = lst.get_head()
    length = 0

    while curr:
        length += 1
        curr = curr.next_element
    return length