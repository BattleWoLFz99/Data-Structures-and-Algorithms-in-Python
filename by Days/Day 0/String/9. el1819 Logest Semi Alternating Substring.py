class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        if len(s) < 3:
            return len(s)
            
        res, cnt = 0, 1
        left = 0
        for right in range(len(s)):
            if right > 0 and s[right] == s[right - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                left = right - 1
                cnt = 2
            # no need to check if never cnt == 3:
            res = max(res, right - left + 1)
            

        return res