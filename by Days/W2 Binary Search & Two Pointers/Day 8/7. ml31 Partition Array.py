class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            # See below for why: Because we are increasing left need limination
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[left], nums[right]
                left += 1
                right -= 1

        return left

s = Solution()
print(s.partitionArray([7,7,9,8,6,6,8,7,9,8,6,6],10))
                                              ^^  No need to do anything