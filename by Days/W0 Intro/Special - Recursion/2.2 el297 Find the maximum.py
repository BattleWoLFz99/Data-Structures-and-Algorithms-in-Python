# 常规版本
class Solution:
    """
    @param nums: the list of numbers
    @return: return the maximum number.
    """
    def maxNum(self, nums):
        return self.max_num(nums, 0, len(nums) - 1)

    def max_num(self, nums, start, end):
        if start > end:
            return float('-inf')

        return max(nums[start], self.max_num(nums, start + 1, end))


# 尾递归
    def maxNum(self, nums):
        return self.max_num(nums, 0, len(nums) - 1, float('-inf'))

    def max_num(self, nums, start, end, result):
        if start > end:
            return result

        result = max(result, nums[start])
        return self.max_num(nums, start + 1, end, result)


# 尾递归的迭代
    def maxNum(self, nums):
        return self.max_num(nums, 0, len(nums) - 1, float('-inf'))

    def max_num(self, nums, start, end, result):
        while True:
            if start > end:
                return result

            next_nums = nums
            next_start, next_end = start + 1, end
            next_result = max(result, nums[start])
            
            nums = next_nums
            start, end = next_start, next_end
            result = next_result