#  The isalnum() returns:
#  True if all characters in the string are alphanumeric
#  False if at least one character is not alphanumeric
#  Below is actually a bad solution
#  Faster than 90%, less than 15%
class Solution:
    def isPalindrome(self, s: str) -> bool:
    	s = [i for i in s.lower() if i.isalnum()]
    	return s == s[::-1]


# Two pointers solution: (Read iString.py #4)
# Runtime faster than 16.28%, memory less than 90%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

# If you don't remember .isalnum(), then:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
    def is_valid(self, char):
        return char.isdigit() or char.isalpha()