class Solution:
    """
    @param A: the array
    @param K: the length 
    @return: the largest subarray
    """
    def largestSubarray(self, A, K):
        def comparetherest(lstA, lstB):
            for i in range(len(lstA)):
                if lstA[i] > lstB[i]:
                    return lstA
                if lstA[i] < lstB[i]:
                    return lstB
            return lstA
        # Write your code here.
        if K >= len(A):
            return A
        lst = A[0:K]
        for i in range(len(A)-K+1):
            if A[i] == lst[0]:
                lst = comparetherest(lst, A[i:i+K])
            if A[i] > lst[0]:
                lst = A[i:i+K]
        return lst

