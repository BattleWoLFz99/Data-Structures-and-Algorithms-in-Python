# Two pointers method practice. O(nlogn) due to sort(). We can write a more efficient solution using hashing.

def two_sum(lst, k):
    # Write your code here
    idx1 = 0
    idx2 = len(lst) - 1
    ans = []
    sum = 0
    lst.sort()
    while (idx1 != idx2):
        sum = lst[idx1] + lst[idx2]
        if sum < k:
            idx1 += 1
        if sum > k:
            idx2 -= 1
        if sum == k:
            ans.append(lst[idx1])
            ans.append(lst[idx2])
            return ans
    return False