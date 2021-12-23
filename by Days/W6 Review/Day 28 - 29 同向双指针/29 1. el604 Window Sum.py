class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if not nums and len(nums) < k:
            return []

        lst_sum = []
        j, window_sum = 0, 0

        for i in range(len(nums)):
            while j < len(nums) and j - i < k:
                window_sum += nums[j]
                j += 1
            if j - i == k:
                lst_sum.append(window_sum)
            window_sum -= nums[i]
            # 可删，但是放在append前面一定错
            # if j >= len(nums):
            #    break
        
        return lst_sum