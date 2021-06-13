class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        if len(s) < 3:
            return len(s)

        left, right = 0, 1
        max_cnt, dup_cnt = 0, 1
        dupped = False

        while right < len(s) - 1:
            if s[right] == s[right - 1]:
                dup_cnt += 1
                right += 1
            else:
                right += 1

            if dup_cnt == 3:
                print([left, right])
                max_cnt = max(right - left, max_cnt)
                left = right - 2
                right = right - 1
                dup_cnt = 1
                dupped = True
                print (max_cnt)
        

        return max_cnt if dupped else len(s)

s = Solution()
print(s.longestSemiAlternatingSubstring("abaaaa"))