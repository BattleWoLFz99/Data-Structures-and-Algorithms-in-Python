# 画图！！！！
class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        if not s or len(s) < k:
            return -1

        counter = dict()
        j, n, ans = 0, len(s), 0
        for i in range(n):
            while j < n and len(counter) < k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                j += 1
            if len(counter) >= k:
                ans = ans + (n - (j - i) + 1) - i
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                del counter[s[i]]

        return ans