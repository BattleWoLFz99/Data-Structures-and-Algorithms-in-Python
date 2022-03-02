from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def max_sub_array(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return 0

        prefix_sum = self.get_prefix_sum(nums)
        min_sum, max_sum = 0, -sys.maxsize
        for end in range(len(nums)):
            max_sum = max(max_sum, prefix_sum[end + 1] - min_sum)
            min_sum = min(min_sum, prefix_sum[end + 1])
        
        return max_sum

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum