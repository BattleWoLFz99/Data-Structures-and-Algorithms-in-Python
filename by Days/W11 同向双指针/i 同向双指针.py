def temp(self, s, k):
    if not s:
        return 0

    counter = dict() # used = [0] * 26
    j, n, answer = 0, len(s), 0
    for i in range(n):
        # i部分：if i 不满足 continue
        # j = max(j, i + 1)

        while j < len(s) and j - i < k:
            counter[s[j]] = counter.get(s[j], 0) + 1 
            j += 1 
        
        # max 一般不用 if
        if j - i == k:
            answer += j - i

        # 常见于 count，if j >= n: break
        # 如果省略 + j 访问下标要注意

        # 为下一个 i 做准备

    return answer