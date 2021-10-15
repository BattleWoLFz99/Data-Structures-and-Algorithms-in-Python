class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def KDifference(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0

        hashing = set()
        cnt = 0

        # 化一下式子，就很简单
        for num in nums:
            if num - target in hashing:
                cnt += 1
            if num + target in hashing:
                cnt += 1
            hashing.add(num)

        return cnt
