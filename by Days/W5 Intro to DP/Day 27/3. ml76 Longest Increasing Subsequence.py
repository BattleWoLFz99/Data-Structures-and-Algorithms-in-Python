class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        
        # state & init
        n = len(nums)
        dp = [1] * n
        
        # func: dp[i] = max(dp[1..i - 1]) + 1 and nums[i] > nums[j]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        # ans
        return max(dp)
        
# 获得一个具体的方案：倒推法