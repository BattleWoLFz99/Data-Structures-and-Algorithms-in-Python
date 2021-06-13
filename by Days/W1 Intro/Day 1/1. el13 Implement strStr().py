class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while (j < len_t):
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1


# KMP to O(n), skip for now