class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        hashset = set()
        for number in numbers:
            if target - number in hashset:
                return number, target - number
            hashset.add(number)
        return [-1, -1]


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        #hash用于建立数值到下标的映射
        hash = {}
        #循环nums数值，并添加映射
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        #无解的情况
        return [-1, -1]