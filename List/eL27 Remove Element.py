class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # write your code here
        while val in nums:
            nums.remove(val)
        return len(nums)

# Using pop()
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # write your code here
        item = 0
        last = len(nums)-1
        while (last>=item):
            if nums[item] == val:
                nums[item],nums[last]=nums[last],nums[item]
                last -= 1
                nums.pop()
            else:
                item += 1
        return item

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # write your code here
        lst = [x for x in nums if x != val]
        return lst