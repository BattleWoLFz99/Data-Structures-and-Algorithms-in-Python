# Foundation of iMerge Sort.py. For the problem, you don't need index, use .append()

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        index, indexA, indexB = 0, 0, 0
        newArr = [0] * (len(A) + len(B))

        while indexA < len(A) and indexB < len(B):
            if A[indexA] < B[indexB]:
                newArr[index] = A[indexA]
                indexA += 1
                index += 1
            else:
                newArr[index] = B[indexB]
                indexB += 1
                index += 1

        while indexA < len(A):
            newArr[index] = A[indexA]
            indexA += 1
            index += 1

        while indexB < len(B):
            newArr[index] = B[indexB]
            indexB += 1
            index += 1
        
        return newArr