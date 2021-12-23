# O(n)
class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        if not s:
            return 0

        counter = {}
        answer = 0
        j = 0
        # maxFreq 以打擂台的方式记录出现最多的字符数量
        max_freq = 0
        for i in range(len(s)):
            # 当j作为下标合法 且 最少需要被替换的字母数目<=k
            while j < len(s) and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1 
                # 更新出现最多的字符数量
                max_freq = max(max_freq, counter[s[j]])
                j += 1 
            
            # 如果替换 除出现次数最多的字母之外的其他字母 的数目>k,
            # 说明有一个不能换，答案与j-i-1进行比较；
            # 否则说明直到字符串末尾替换数目都<=k，可以全部换掉 
            # 答案与子串长度j-i进行比较
            if j - i - max_freq > k:
                # i ~ j - 1 的 substring 需要 k + 1 次替换
                # i ~ j - 2 的substring 只需要 k 
                answer = max(answer, j - 1 - i)
            # 如果是因为 j == len(s) 出来的:
            else:
                # i ~ j - 1 的 substring <= k 替换
                answer = max(answer, j - i) 
                
            # 起点后移一位，当前起点位置的字母个数-1
            counter[s[i]] -= 1
            max_freq = max(counter.values())
        return answer