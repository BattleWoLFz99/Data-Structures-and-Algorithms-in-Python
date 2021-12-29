class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        hashing = set()
        j = 0
        n = len(s)
        answer = 0
        for i in range(n):
            while j < n and s[j] not in hashing:
                hashing.add(s[j])
                j += 1
            answer = max(j - i, answer)
            hashing.remove(s[i])
            if j >= n:
                break        
                
        return answer
                