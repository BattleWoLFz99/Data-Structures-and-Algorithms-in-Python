# 我也不知道为什么这题出现在这里？
# arr.sort(reverse = True) 后跟 for ！！

class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """
    def minElements(self, arr):
        if not arr:
            return

        arr.sort(reverse = True)
        left_sum = 0
        right_sum = sum(arr)

        for i in range(len(arr)):
            left_sum += arr[i]
            right_sum -= arr[i]
            if left_sum > right_sum:
                return i + 1

        return 



