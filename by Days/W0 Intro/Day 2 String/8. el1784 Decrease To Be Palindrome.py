class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        if s is None:
            return 0

        left, right = 0, len(s) - 1
        count = 0
        while left < right:
            count += abs(ord(s[left]) - ord(s[right]))
            left += 1
            right -= 1

        return count
        

# 记得可以用find就是了：
class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """

    def numberOfOperations(self, s):
        charset = 'abcdefghijklmnopqrstuvwxyz'
        left, right = 0, len(s) - 1
        cnt = 0
        while left < right:
            cnt += abs(charset.find(s[left]) - charset.find(s[right]))
            left += 1
            right -= 1
        return cnt