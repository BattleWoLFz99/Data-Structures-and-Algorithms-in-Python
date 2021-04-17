# Sample Input [10,-1,20,4,5,-9,-6]
# Sample Output [-1,-9,-6,10,20,4,5]

#Solution 1:
def rearrange(lst):
    neg = []
    pos = []
    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
    return neg + pos

# Solution 2: Pythonic
def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]