# if start < end can be deleted, add it for habit(it is actually important)
# Stop using s[::-1], that is why jump right into Leetcode is bad...
# s.isdigit()     s.isalpha()
# for c in s:

# 三刷：用 left right 啊卧槽？然后需要注意的是别忘了动双指针在判断之后
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum() :
                start += 1
            while start < end and not s[end].isalnum() :
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True