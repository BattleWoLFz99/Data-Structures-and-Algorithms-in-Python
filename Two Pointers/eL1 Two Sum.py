# You may also find hashing solutions in different folders.
# Modified, return two values:

class Solution:
    def twoSum(Self, numbers, target):
        numbers.sort()
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left -= 1
            else:
                return numbers[left], numbers[right]
        return [-1, -1]

#Leetcode ver.
class Solution:
    def twoSum(Self, numbers, target):
        if not numbers:
            return [-1, -1]

        nums = [
            (number, index)
            for index, number in enumerate(numbers)
        ]
        # nums = []
        # for index, numer in enumerate(numbers):
        #    nums.append((number, index))

        nums.sort()
        # two-dimension array, compare the first number first, if equals, then the second number


        numbers.sort()
        left, right = 0, len(numbers) - 1
        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left -= 1
            else:
                return sorted(numbers[left][1], numbers[right][1])
        return [-1, -1]