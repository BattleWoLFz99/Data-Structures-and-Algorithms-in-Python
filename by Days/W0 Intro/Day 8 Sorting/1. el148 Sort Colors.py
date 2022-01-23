class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        self.partition_array(nums, 1)
        self.partition_array(nums, 2)

    def partition_array(self, nums, k):
        last_small_pointer = -1
        for i in range(len(nums)):
            if nums[i] < k:
                last_small_pointer += 1
                nums[last_small_pointer], nums[i] = \
                nums[i], nums[last_small_pointer]

# One time traversal:
    def sortColors(self, nums):
        zero_pointer = -1
        two_pointer = len(nums)
        i = 0
        while i < len(nums) and i < two_pointer:
            if nums[i] == 0:
                zero_pointer += 1
                nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i]
            elif nums[i] == 2:
                two_pointer -= 1
                nums[i], nums[two_pointer] = nums[two_pointer], nums[i]
                i -= 1
            i += 1