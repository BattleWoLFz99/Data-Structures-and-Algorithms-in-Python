class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def fourSumCount(self, A, B, C, D):
        # Write your code here
        dictionary = {}

        for a in A:
            for b in B:
                total = a + b
                dictionary[total] = dictionary.get(total, 0) + 1

        cnt = 0

        for c in C:
            for d in D:
                total = c + d
                cnt += dictionary.get(-total, 0)

        return cnt