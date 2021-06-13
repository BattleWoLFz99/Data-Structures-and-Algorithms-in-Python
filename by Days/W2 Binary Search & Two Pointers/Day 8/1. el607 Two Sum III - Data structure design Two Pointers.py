# Not the most optimal, please also check /hashing/
# Two pointers practice, also a good template
# Keep in mind that:
#   target - eachEle  takes O(n)
#   Binary Search takes O(logn)
#   So total: O(nlogn)
# That is why I used two pointers here, for practice purpose.

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.nums = []

    def add(self, number):
        # write your code here
        self.nums.append(number)
        index = len(self.nums) - 1

        while index > 0 and self.nums[index - 1] > self.nums[index]:
            self.nums[index - 1], self.nums[index] = \
            self.nums[index], self.nums[index - 1]
            index -= 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < value:
                left += 1
            elif two_sum > value:
                right -= 1
            else:
                return True

        return False

# TLE. Go under /hashing/