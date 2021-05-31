# set(): Duplicates Not Allowed

#Sample Input #
#list1 = [9,4,7,1,-2,6,5]
#list2 = [7,1,-2]
#Sample Output #
#True

def is_subset(list1, list2):
    # Write your code here
    s = set(list1)
    for elem in list2:
        if elem not in s:
            return False
    return True