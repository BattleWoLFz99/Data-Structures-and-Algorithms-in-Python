# left >= right 就是 Palindrome 了
class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        left, right = self.twoPointer(s, 0, len(s) - 1)            
        if left >= right:
            return True
            
        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

    def isPalindrome(self, s, left, right):
        left, right = self.twoPointer(s, left, right)
        return left >= right
        
    def twoPointer(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right


# two def, use _ since you don't care about the return:
class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        if not s:
            return True

        flag, left, right = self.is_palindrome(s, 0, len(s) - 1)

        if flag:
            return True

        flag_left, _, _ = self.is_palindrome(s, left + 1, right)
        flag_right, _, _ = self.is_palindrome(s, left, right - 1)

        return flag_left or flag_right

    def is_palindrome(self, s, left, right):
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False, left, right
            left += 1
            right -= 1
        
        return True, left, right