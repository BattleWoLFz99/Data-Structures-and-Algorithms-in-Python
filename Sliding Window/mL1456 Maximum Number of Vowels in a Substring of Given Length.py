class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        
        vowels = "aeiou"
        count = 0
        j, answer = 0, 0
        for i in range(len(s)):
            while j < len(s) and j - i < k:
                if s[j] in vowels:
                    count += 1
                j += 1
            
            if j - i >= k:
                answer = max(count, answer)
            
            if s[i] in vowels:
                count -= 1
            
        return answer