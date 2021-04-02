def merge_lists(lst1, lst2):
    # list.insert(index, obj)
    # list.extend(iterable) - list, set, tuple, etc.
    ind1 = 0
    ind2 = 0
    while ind1 < len(lst1) and ind2 < len(lst2):
        if lst1[ind1] > lst2[ind2]:
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1+=1
    if ind2 < len(lst2):
        lst1.extend(lst2[ind2:])
    return lst1
