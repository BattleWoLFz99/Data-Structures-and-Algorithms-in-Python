# QuickSort is slower, dont
# Counting Sort ver.
# Uses extra space

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        if nums is None or len(nums) == 0:
            return

        color_cnts = [0] * 3

        for num in nums:
            color_cnts[num] += 1
        
        index = 0

        for i in range(len(color_cnts)):
            cnt = color_cnts[i]
            while cnt > 0:
                nums[index] = i
                cnt -= 1
                index += 1

# Best solution:

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        self.partition_array(nums, 1)
        self.partition_array(nums, 2)

    def partition_array(self, nums, k):
        # Pointing to the last ele of <k area
        last_small_pointer = -1
        for i in range(len(nums)):
            if nums[i] < k:
                last_small_pointer += 1
                nums[last_small_pointer], nums[i] = \
                nums[i], nums[last_small_pointer]

# or, it increases your logic complexity, do this only as follow-up(or never)

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        last = self.partition_array(nums, 1, -1)
        self.partition_array(nums, 2, last)

    def partition_array(self, nums, k, last_small_pointer):
        # Pointing to the last ele of <k area
        for i in range(last_small_pointer+1, len(nums)):
            if nums[i] < k:
                last_small_pointer += 1
                nums[last_small_pointer], nums[i] = \
                nums[i], nums[last_small_pointer]

        return last_small_pointer


# One partition, absolutely not recommended

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        left, right = 0, len(nums) - 1
        index = 0

        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1