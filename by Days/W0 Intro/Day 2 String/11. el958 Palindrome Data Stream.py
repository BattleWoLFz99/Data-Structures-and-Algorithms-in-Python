class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        if s is None or len(s) == 0:
            return None

        results = [0 for _ in range(len(s))]
        letters = [0 for _ in range(26)]
        odd_letter_count = 0
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            if letters[ord(s[i]) - ord('a')] % 2 == 1:
                odd_letter_count += 1
            else:
                odd_letter_count -= 1
            results[i] = 0 if odd_letter_count > 1 else 1

        return results