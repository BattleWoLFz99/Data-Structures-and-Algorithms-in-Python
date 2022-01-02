class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        n, count = len(nums), 0
        for i in range(n):
            if nums[i] == 0:
                count += 1
                
        j = 0
        for i in range(n):
            j = max(j, i + 1)
            while j < n and nums[j] == 0:
                j += 1
            if j >= n:
                break
            else:
                nums[i] = nums[j]
                j += 1
        
        k = n - 1
        while count > 0:
            nums[k] = 0
            k -= 1
            count -= 1

        print (nums)
s = Solution()
s.moveZeroes([1])