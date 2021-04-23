# Don't use [i:j:-1], you can only write:
# return s[left:right]==s[right-1:left-1:-1] or s[left+1:right+1]==s[right:left:-1]
# However, left can be 0...
# So, define ur own isPalindrome, easiest... Spent way too much time on [left:right:-1]
# Like, s[left:right:-1] returns a empty string...

# While it is not really a big deal in terms of time and space complexity, it increases
# the Logicality complexity. You have to think very carefully for bug free and edge 
# cases, which, you should really avoid. (See iPython.py)

# Faster than 82%, less than 73% (It creates new string)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(string):
            return string==string[::-1]
            
        if s is None:
            return False
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                if left + 2 > right:
                    return True
                else:
                    return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
            left += 1
            right -= 1
        
        return True


#  From jiuzhang, faster than 45.68%, less than 99% (No new string is created)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s is None:
            return False
        
        left, right = self.findDifference(s, 0, len(s) - 1)
        if left >= right:
            return True
        
        return self.isPalindrome(s, left + 1, right) or\
        self.isPalindrome(s, left, right - 1)
    
    def isPalindrome(self, s, left, right):
        left, right = self.findDifference(s, left, right)
        return left >= right
    
    def findDifference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right