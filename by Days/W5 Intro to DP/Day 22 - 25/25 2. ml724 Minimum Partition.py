class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
    def findMin(self, nums):
        if not nums:
            return 

        target = sum(nums) // 2
        n = len(nums)

        # state
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # init
        dp[0][0] = True

        # function
        for i in range(1, n + 1):
            for j in range(target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        closed_target = 0
        for j in range(target, -1, -1):
            if dp[n][j]:
                closed_target = j
                break
                
        return sum(nums) - 2 * closed_target