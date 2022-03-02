# Stars and Bars + Sliding Window

class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def PickApples(self, A, K, L):
        if K + L > len(A):
            return -1
        
        n, max_apples = len(A), float('-inf')
        for i in range(n):
            left_K_max = self.get_max(A, 0, i, K)
            right_L_max = self.get_max(A, i, n, L)
            if left_K_max != -1 and right_L_max != -1:
                max_apples = max(max_apples, left_K_max + right_L_max)

            left_L_max = self.get_max(A, 0, i, L)
            right_K_max = self.get_max(A, i, n, K)
            if left_L_max != -1 and right_K_max != -1:
                max_apples = max(max_apples, left_L_max + right_K_max)

        if max_apples == float('-inf'):
            return -1
        return max_apples

    def get_max(self, A, start, end, interval):
        if end - start < interval:
            return -1

        j, curr_max_apples, curr_apples = start, 0, 0
        for i in range(start, end):
            while j < end and j - i < interval:
                curr_apples += A[j]
                j += 1
            if j - i == interval:
                curr_max_apples = max(curr_max_apples, curr_apples)
            #else:
                #break
            curr_apples -= A[i]
            
        return curr_max_apples