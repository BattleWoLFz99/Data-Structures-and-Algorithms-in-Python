class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # 重点1：任何代码都要进行异常检测
        if not s:
            return ""
        
        # 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        longest = ""
        for middle in range(len(s)):
            # 重点3：子函数化避免重复代码
            sub = self.find_palindrome_from(s, middle, middle)
	        # 重点4：通过返回值来避免使用全局变量这种不好的代码风格
            if len(sub) > len(longest):
                longest = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub
                
		# 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        return longest
        
    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string):
            # 重点5：将复杂判断拆分到 while 循环内部，而不是放在 while 循环中，提高代码可读性
            if string[left] != string[right]:
                break
            left -= 1
            right += 1
            
        return string[left + 1:right]