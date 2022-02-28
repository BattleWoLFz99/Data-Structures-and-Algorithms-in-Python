# 模板起手
j = 0
for i in range(n):
    while j < n and i, j的搭配不满足条件:
        j += 1
    if j >= n:
        break
    处理 i, j 这次搭配

# 6-8 也许能写两个 if，也许是 if else，例如ml386，ml1246

# 要不要 j = max(i + 1, j):
# 助教 - 技工：大多数题目不需要。一般而言，做题的时候先不写这个，然后做的时候再看会不会
# 出现计算空区间甚至负区间，再考虑要不要 j = max(i + 1, j) 或者是 j = max(i, j)
# j = 0 模板起手
# 那些需要加的，写的时候，一般考虑到要么是不允许 i = j（两数之差）就 j = max(i + 1, j)
# 要么是前一步可能是空区间，然后左指针移动结果 i 到 j 右边。


# 在 j 停下来的时候，j 是第一个不满足的。不行自己去画。。
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

    j, answer = 0, 0
    n = len(colors)
    for i in range(n):
        # 1. 控制 i 的条件。i 不满足要 continue 很正常。那么就很容易跳 j 后面要带 3.
        # 2. 可能要处理 i - 1，放上一层最后也 ok
        if i < n - 1 and colors[i] != colors[i + 1]:
            continue
        # 2. 可能 i 要跳到 j 的位置，或者 j 的后面
        if i < j:
            continue

        # 3. 可选。具体见上面。瞎带你就等着给双指针写 visited 吧
        j = max(i + 1, j)
        # 4. 后面一定每题都不一样
        while j < n and colors[j] == colors[i]:
            # 5. 可能要更新例如 max_freq
            j += 1

        # 5. 处理这次 i j 的搭配
        answer += sum(neededTime[i:j]) - max(neededTime[i:j])

        # 6. 写在这里过，写在 5. 前面过，也省略过
        if j >= n:
            break

        # 7. 5 + 6 可能会写成 if else，如 j - 1 是第一个不满足位置 j - 2 是最大位置
            
    return answer


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        j, answer = 0, 0
        n = len(s)
        used = [False for _ in range(129)]
        for i in range(n):
            # i 的私人空间只处理 i
            # 这里单独处理了 i - 1
            if i > 0:
                used[ord(s[i - 1])] = False
            # 把逻辑捋清楚，把 i 扔进 used。这里错在if外面单独写了0，然后搞不清楚了
            # 后面加了 if，因为要处理别的最多几个不一样的字符题目。。
            if not used[ord(s[i])]:
                used[ord(s[i])] = True

            # j 的私人空间只处理 j，且 j 位置一定是不满足的，注意别写反了
            # 不要在当前层去考虑下一层的事情
            j = max(j, i + 1)
            while j < n and not used[ord(s[j])]:
                used[ord(s[j])] = True
                j += 1

            answer = max(answer, j - i)

            if j >= n:
                break
            
        return answer


# 另一种常见写法是ml1246 与 ml 386：
# j - 1 是第一个不满足位置，因此最大位置是 j - 2
# 出去的时候要 if else
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


# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# 思路：模板起手，发现只能写 >= 那就不能 i == j 必须 j = i + 1 了
# 然后又发现一旦不搭配 i 要到飞到 j 位置所以 i < j continue 同时更新最大值
# j 出去了可以 break
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        if not nums:
            return
        
        n = len(nums)
        j, left_max, curr_max = 0, nums[0], nums[0]
        for i in range(n):
            # 第三步想 i 要不要飞到 j 还是 一步步走，要飞就必须带 max
            if i < j:
                continue
            j = max(i + 1, j)
                            # 第一步肯定先想这里怎么写
            while j < n and nums[j] >= left_max:
                if nums[j] > curr_max:
                    curr_max = nums[j]
                j += 1
            # 第二步肯定想两个退出条件
            if j >= n:
                break  
            if curr_max > left_max:
                left_max = curr_max
        
        # 完了在考虑 return i + 1 if i + 1 <= n else i 笑死。。从来没有这样过
        # 同向双指针是最容易出错的多刷题目吧
        return i + 1