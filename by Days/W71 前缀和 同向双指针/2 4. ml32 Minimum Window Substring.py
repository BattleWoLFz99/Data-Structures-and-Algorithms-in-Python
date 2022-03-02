# 配合 Day 28 29
# 还有384, 328

class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        if len(target) == 0:
            return ""
        
        target_count, target_len, curr_count = [0] * 127, len(target), [0] * 127
        for char in target:
            target_count[ord(char) - ord('0')] += 1

        j, n, matched_count = 0, len(source), 0
        curr_len, min_len, start_index = 0, float('inf'), 0
        for i in range(n):
            while j < n and matched_count < target_len:
                curr_count[ord(source[j]) - ord('0')] += 1
                if target_count[ord(source[j]) - ord('0')] == \
                    curr_count[ord(source[j]) - ord('0')]:
                    matched_count += target_count[ord(source[j]) - ord('0')]
                j += 1
            if matched_count == target_len:
                curr_len = j - i
                if curr_len < min_len:
                    min_len = curr_len
                    start_index = i
            if target_count[ord(source[i]) - ord('0')] == \
                curr_count[ord(source[i]) - ord('0')]:
                matched_count -= target_count[ord(source[i]) - ord('0')]
            curr_count[ord(source[i]) - ord('0')] -= 1
        
        if min_len == float('inf'):
            return ""
        return source[start_index:start_index + min_len]