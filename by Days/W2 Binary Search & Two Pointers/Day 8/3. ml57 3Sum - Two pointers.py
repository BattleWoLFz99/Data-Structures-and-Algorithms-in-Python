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
            # no need for while left < right, because it is sorted
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1