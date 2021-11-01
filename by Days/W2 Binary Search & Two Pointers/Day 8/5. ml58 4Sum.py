class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    
    Given an array S of n integers, are there elements a, b, c, and d in S such
    that a + b + c + d = target?
    Find all unique quadruplets in the array which gives the sum of target.

    Example 2:

    Input:

    numbers = [1,0,-1,0,-2,2]
    target = 0
    Output:

    [[-1, 0, 0, 1],[-2, -1, 1, 2],[-2, 0, 0, 2]]

    """
    def fourSum(self, numbers, target):
        # write your code here
        results = []

        if not numbers or len(numbers) < 4:
            return results

        numbers.sort()
        length = len(numbers)
        for i in range(0, length - 3):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            for j in range(i + 1, length - 2):
                 # j != i + 1
                if j > i + 1 and numbers[j] == numbers[j-1]:
                    continue
                self.two_sum(numbers, i, j, target, results)

        return results

    def two_sum(self, numbers, i, j, target, results):

        left = j + 1
        right = len(numbers) - 1
        sum_num = target - numbers[i] - numbers[j]

        while left < right:
            if numbers[left] + numbers[right] == sum_num:
                results.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left-1]:
                    left += 1
                while left < right and numbers[right] == numbers[right+1]:
                    right -= 1
            elif numbers[left] + numbers[right] < sum_num:
                left += 1
            else:
                right -= 1