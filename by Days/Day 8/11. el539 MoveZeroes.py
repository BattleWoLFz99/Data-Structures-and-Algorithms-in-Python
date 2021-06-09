class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        fillPointer, movePointer = 0, 0
        while movePointer < len(nums):
            if nums[movePointer] != 0:
                if fillPointer != movePointer:
                    nums[movePointer], nums[fillPointer] = \
                    nums[fillPointer], nums[movePointer]
                fillPointer += 1
            movePointer += 1

# To minimize the total number of operations:
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        fillPointer, movePointer = 0, 0
        while movePointer < len(nums):
            if nums[movePointer] != 0:
                if fillPointer != movePointer:
                    nums[fillPointer] = nums[movePointer]
                fillPointer += 1
            movePointer += 1

        while fillPointer < len(nums):
            if nums[fillPointer] != 0:
                nums[fillPointer] = 0
            fillPointer += 1