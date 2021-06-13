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