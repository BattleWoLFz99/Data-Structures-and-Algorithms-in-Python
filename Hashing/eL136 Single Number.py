class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashing = set()
        for num in nums:
            if num not in hashing:
                hashing.add(num)
            else:
                hashing.remove(num)
        return hashing.pop() # or min(hashing)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = set(nums)
        return 2 * sum(hash) - sum(nums)