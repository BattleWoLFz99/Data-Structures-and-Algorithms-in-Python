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


class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def stringCount(self, str):
        if not str:
            return 0

        j, answer = 0, 0
        n = len(str)
        for i in range(n):
            if str[i] != '0' or i < j:
                continue
            j = max(i + 1, j)
            while j < n and str[j] == '0':
                j += 1
            answer += self.get_count(j - i)
            if j >= n:
                break

        return answer

    def get_count(self, count):
        return (1 + count) * count // 2