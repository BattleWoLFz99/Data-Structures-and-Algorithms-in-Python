# Ver 1, TLE
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        if s is None or p is None:
            return False

        return self.helper(s, 0, p, 0)

    def helper(self, s, s_index, p, p_index):
        if p_index == len(p):
            return s_index == len(s)
        if s_index == len(s):
            return self.all_star(p, p_index)

        s_char = s[s_index]
        p_char = p[p_index]

        if p_char != '*':
            return self.is_match(s_char, p_char) and \
            self.helper(s, s_index + 1, p, p_index + 1)

        for new_s_index in range(s_index, len(s) + 1):
            if self.helper(s, new_s_index, p, p_index + 1):
                return True

        return False

    def all_star(self, p, p_index):
        for i in range(p_index, len(p)):
            if p[i] != '*':
                return False
        return True

    def is_match(self, s_char, p_char):
        return s_char == p_char or p_char == '?'


# 仔细拆下去，for 拆出来的 与 吃与不吃 拆出来的是一样的
# 例如 abc 与 *bc 的拆解，与 bc 与 *bc 的拆解，其实是有包含关系
# abc 与 *bc，不吃就是 abc 与 bc，吃就是 bc 与 *bc
# 于是就有了Ver 2。然而还是 TLE, 还 TLE 在了同一个地方
    def isMatch(self, s, p):
        if s is None or p is None:
            return False

        return self.helper(s, 0, p, 0)

    def helper(self, s, s_index, p, p_index):
        if p_index == len(p):
            return s_index == len(s)
        if s_index == len(s):
            return self.all_star(p, p_index)

        s_char = s[s_index]
        p_char = p[p_index]

        if p_char != '*':
            return self.is_match(s_char, p_char) and \
            self.helper(s, s_index + 1, p, p_index + 1)

        return self.helper(s, s_index, p, p_index + 1) or \
        self.helper(s, s_index + 1, p, p_index)

    def all_star(self, p, p_index):
        for i in range(p_index, len(p)):
            if p[i] != '*':
                return False
        return True

    def is_match(self, s_char, p_char):
        return s_char == p_char or p_char == '?'


# 真正低效的地方在 * 很多的时候，也就是一分为二很多的时候，会有吃与不吃，不吃与吃
# 挺像 Triangle 的，(x, y) -> (x + 1, y) or (x + 1, y + 1) -> 重复(x + 2, y + 1)
# memo[(s_index, p_index)] = True/False
    def isMatch(self, s, p):
        if s is None or p is None:
            return False

        return self.helper(s, 0, p, 0, {})

    def helper(self, s, s_index, p, p_index, memo):
        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]
        if p_index == len(p):
            return s_index == len(s)
        if s_index == len(s):
            return self.all_star(p, p_index)

        s_char = s[s_index]
        p_char = p[p_index]

        if p_char != '*':
            return self.is_match(s_char, p_char) and \
            self.helper(s, s_index + 1, p, p_index + 1, memo)

        match = \
        self.helper(s, s_index, p, p_index + 1, memo) or \
        self.helper(s, s_index + 1, p, p_index, memo)
        memo[(s_index, p_index)] = match
        return match

    def all_star(self, p, p_index):
        for i in range(p_index, len(p)):
            if p[i] != '*':
                return False
        return True

    def is_match(self, s_char, p_char):
        return s_char == p_char or p_char == '?'


# 上面的是最优解，想不出拆分Ver 1 直接 memo的
# 状态总数还是 n^2，计算每个状态上面是O(1)，这里是O(n)。多了一个 n
    def isMatch(self, s, p):
        if s is None or p is None:
            return False

        return self.helper(s, 0, p, 0, {})

    def helper(self, s, s_index, p, p_index, memo):
        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]
        if p_index == len(p):
            return s_index == len(s)
        if s_index == len(s):
            return self.all_star(p, p_index)

        s_char = s[s_index]
        p_char = p[p_index]

        if p_char != '*':
            return self.is_match(s_char, p_char) and \
            self.helper(s, s_index + 1, p, p_index + 1, memo)

        for new_s_index in range(s_index, len(s) + 1):
            match = self.helper(s, new_s_index, p, p_index + 1, memo)
            memo[(new_s_index, p_index + 1)] = match
            if match:
                return True

        memo[(s_index, p_index)] = False
        return False

    def all_star(self, p, p_index):
        for i in range(p_index, len(p)):
            if p[i] != '*':
                return False
        return True

    def is_match(self, s_char, p_char):
        return s_char == p_char or p_char == '?'