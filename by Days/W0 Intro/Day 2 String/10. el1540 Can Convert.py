# For i in 要找的那一个，aka 短的那一个；j 给长的那个
# 不然
# s = "lintcode"
# t = "code"
# 直接就出去了

class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        if not s or not t:
            return False

        j, count = 0, 0
        for i in range(len(t)):
            while j < len(s) and t[i] != s[j]:
                j += 1
            if j >= len(s):
                break
            j += 1
            count += 1

        return count ==  len(t)