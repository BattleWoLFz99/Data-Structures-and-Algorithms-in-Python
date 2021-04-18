# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list 
# such that the 0th index will have the largest number, the 1st index will have the smallest, 
# and the 2nd index will have second-largest, and so on. In other words, all the even-numbered 
# indices will have the largest numbers in the list in descending order and the odd-numbered indices 
# will have the smallest numbers in ascending order.

#Sample Input lst = [1,2,3,4,5]
#Sample Output lst = [5,1,4,2,3]

def max_min(lst):
    # Write your code here
    if len(lst) <= 1:
        return lst
    minIdx = 0
    maxIdx = len(lst) - 1
    maxminlst = []
    while minIdx < maxIdx:
        maxminlst.append(lst[maxIdx])
        maxminlst.append(lst[minIdx])
        minIdx += 1
        maxIdx -= 1
    if (len(lst) % 2) != 0:
        maxminlst.append(lst[maxIdx])
    return maxminlst