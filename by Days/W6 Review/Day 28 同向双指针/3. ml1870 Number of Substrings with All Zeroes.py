class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def stringCount(self, str):
        if not str:
            return 0

        j, answer = 1, 0
        for i in range(len(str)):
            if str[i] != '0':
                continue
            j = max(j, i + 1)
            while j < len(str) and str[j] == '0':
                j += 1
            answer += j - i

        return answer