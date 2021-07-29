class Solution:
    
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        if not nums:
            return [-1, -1]

        target = abs(target)
        n = len(nums)
        j = 1

        for i in range(n):
            j = max(j, i + 1)
                            # i, j的搭配不满足条件
            while j < n and nums[j] - nums[i] < target:
                j += 1
            if j >= n:
                break
            # 处理 i, j 这次搭配
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]

        return [-1, -1]