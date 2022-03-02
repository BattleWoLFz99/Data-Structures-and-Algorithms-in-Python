# 前缀和 + 哈希
class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """
    def searchSubarray(self, arr, k):
        sum_to_index = dict()
        sum_to_index[0] = -1
        prefix_sum = 0
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum - k in sum_to_index:
                return i - sum_to_index[prefix_sum - k]
            # 返回最近的
            if prefix_sum not in sum_to_index:
                sum_to_index[prefix_sum] = i

        return -1


# 求前缀和，没找到单独题。。
    def get_prefix_sum(self, arr):
        prefix_sum = [0]
        for num in arr:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum