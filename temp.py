class Solution:
    """
    @param a: A number
    @return: Returns the maximum number after insertion
    """
    def get_prefix_sum(self, arr):
        n = len(arr)
        prefix_sum = [0] * (len(arr) + 1)
        prefix_sum[0] = 0
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
            
        return prefix_sum

s = Solution()
print(s.get_prefix_sum([1,2,3,4,5]))