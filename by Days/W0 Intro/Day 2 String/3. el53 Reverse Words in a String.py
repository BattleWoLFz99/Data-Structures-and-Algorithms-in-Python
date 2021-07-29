# s = "  "    AttributeError: 'list' object has no attribute 'reversed'

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        #strip()去掉s头尾的空格，split()按照空格分割字符串，reversed翻转，''.join按照空格连接字符串
        return ' '.join(reversed(s.strip().split()))