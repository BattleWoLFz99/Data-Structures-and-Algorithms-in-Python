class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0
        
        if k >= len(s):
            return len(s)

        counter = {}
        answer = 0
        j = 0
        for i in range(len(s)):
            while j < len(s) and len(counter) <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1 
                j += 1 

            if len(counter) > k:
                answer = max(answer, j - i - 1)
            else:
                answer = max(answer, j - i)

            counter[s[i]] -= 1 
            if counter[s[i]] == 0:
                del counter[s[i]]

        return answer