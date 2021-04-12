class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # write your code here
        while val in nums:
            nums.remove(val)
        return len(nums)