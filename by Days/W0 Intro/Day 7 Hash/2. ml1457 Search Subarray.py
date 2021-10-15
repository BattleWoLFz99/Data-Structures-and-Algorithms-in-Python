# dict[we want to find] = location

class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """
    def searchSubarray(self, arr, k):
        if not arr:
            return 

        d = dict()
        d[0] = -1
        prefix_sum = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum - k in d:
                return i - d[prefix_sum - k]
            if prefix_sum not in d:
                d[prefix_sum] = i

        return -1
