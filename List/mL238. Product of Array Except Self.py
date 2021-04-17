# Version 1 TLE: O(n2). Absolutely skip the most basic solution let us call it version 0 without left variable

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        left = 1
        for i in range(len(nums)):
            currentproduct = 1
            for k in range(i+1,len(nums)):
                currentproduct *= nums[k]
            currentproduct *= left
            result.append(currentproduct)
            left *= nums[i]
        return result

# Version 2: O(n) Solution that only faster than 21%
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        left = 1
        productleft = []
        for ele in nums:
            productleft.append(left)
            left = left * ele
        right = 1
        productright = []
        for ele in nums[::-1]:
            productright.append(right)
            right = right * ele
        for i in range(len(nums)):
            result.append(productleft[i]*productright[len(nums)-1-i])
        return result

# Version 3: We can optimize line 27-32, just like how we did in solution 1. Faster than 82%
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        product = []
        for ele in nums:
            product.append(left)
            left = left * ele
        right = 1
        for i in range(len(nums)-1,-1,-1):
            product[i] = product[i] * right
            right = right * nums[i]
        return product
