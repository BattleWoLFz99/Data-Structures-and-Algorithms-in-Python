class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero. 
    and A<=B<=C
    Q: what is the format of the return
    Q: will there be any duplicated numbers? Should I remove all duplicated answers?
    """
    def threeSum(self, numbers):
        # write your code here
        results = []

        if not numbers or len(numbers) < 3:
            return results

        numbers.sort()
        length = len(numbers)

        for i in range(0, length - 2):
            # already sorted, remove duplicated numbers, better than i + 1
            if i > 0 and numbers[i] == numbers[i-1]:
                continue

            left = i + 1
            right = length - 1
            target = -numbers[i]

            self.find_two_sum(numbers, left, right, target, results)

        return results

    def find_two_sum(self, numbers, left, right, target, results):
        while left < right:
            if numbers[left] + numbers[right] == target:
                results.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                # Remove duplicated
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            # no need for while left < right
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1



# Linghu Ver.
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        nums = sorted(nums)
        
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], results)
            
        return results

    def find_two_sum(self, nums, left, right, target, results):
        last_pair = None
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    results.append([-target, nums[left], nums[right]])
                last_pair = (nums[left], nums[right])
                right -= 1
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1