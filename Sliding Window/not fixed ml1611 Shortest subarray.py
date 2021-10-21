# 基础滑动窗口
min_length = float('inf')
j = 0
for i in range(len(nums)):
    while j < len(nums) and 不满足条件:
        subarray_sum += nums[j]
        j += 1

    if 满足 subarray_sum >= k:
        min_length = min(min_length, j - i) 
         
    动左指针 subarray_sum -= nums[i]


class Solution:
    """
    @param nums: 
    @param k: 
    @return: return the length of shortest subarray
    """
    def smallestLength(self, nums, k):
        # Write your code here
        if not nums:
            return -1

        min_length = float('inf')
        j = 0
        subarray_sum = 0
        for i in range(len(nums)):
            while j < len(nums) and subarray_sum < k:
                subarray_sum += nums[j]
                j += 1
            
            if subarray_sum >= k:
                min_length = min(min_length, j - i)
            
            subarray_sum -= nums[i]

        return min_length if min_length != float('inf') else -1