上给的模板
j = 1
for i in range(n):
    while j < n and i, j的搭配不满足条件:
        j += 1
    if j >= n:
        break
    处理 i, j 这次搭配

# 在 j 停下来的时候，j 是第一个不满足的。不行自己去画。。
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

    j, answer = 0, 0
    n = len(colors)
    for i in range(n):
        # 1. 控制 i 的条件
        if i < n - 1 and colors[i] != colors[i + 1]:
            continue
        # 2. 可能 i 要跳到 j 的位置，或者 j 的后面
        if i < j:
            continue

        # 3. 必写，因为 j 从 0 开始。至今无错
        j = max(i + 1, j)
        # 4. 后面一定每题都不一样
        while j < n and colors[j] == colors[i]:
            j += 1

        # 5. 处理这次 i j 的搭配
        answer += sum(neededTime[i:j]) - max(neededTime[i:j])

        # 6. 写在这里过，写在 5. 前面过，也省略过
        if j >= n:
            break
            
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