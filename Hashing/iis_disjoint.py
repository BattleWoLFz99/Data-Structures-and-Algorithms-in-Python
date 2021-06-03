#Output #
#It returns True if the two are disjoint. Otherwise, it returns False.

#Sample Input #
#list1 = [9,4,3,1,-2,6,5]
#list2 = [7,10,8]
#Sample Output #
#True


def is_disjoint(list1, list2):
    s = set(list1)
    for elem in list2:
        if elem in s:
            return False
    return True

# or
def is_disjoint(list1, list2):
    # Write your code here
    s1 = set(list1)
    s2 = set(list2)

    if len(s1 & s2) == 0:
        return True
    else:
        return False