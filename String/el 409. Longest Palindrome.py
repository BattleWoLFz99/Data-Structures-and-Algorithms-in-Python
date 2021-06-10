class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        
        hash = {}
        
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True
                
        odd_count = len(hash)
        if odd_count > 0:
            odd_count -= 1
            
        return len(s) - odd_count