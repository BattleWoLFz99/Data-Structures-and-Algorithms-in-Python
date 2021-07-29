# Use Python，你直接str.upper() 就好了。。
# Input: str = "abC12"
# Output: "ABC12"

class Solution:
    # @param {string} str a string
    # @return {string} a string
    def lowercaseToUppercase2(self, str):
        return str.upper()


class Solution:
    # @param {string} str a string
    # @return {string} a string
    def lowercaseToUppercase2(self, str):
        # Write your code here
        p = list(str)
        #遍历整个字符串，将所有的小写字母转成大写字母
        for i in range(len(p)):
            if p[i] >= 'a' and p[i] <= 'z':
                p[i] = chr(ord(p[i]) - 32)
        return ''.join(p)