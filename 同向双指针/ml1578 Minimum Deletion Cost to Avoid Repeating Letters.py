# 这鸟模板是真的难用。。。。是变数很多的模板，所以抽象后缺少很多细节
# 还是喜欢 while 手控唉。。
# 这里 if continue 是变数，if j越界也是变数， j = max(j, i + 1) 是核心

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 0
    
        j, answer = 1, 0
        for i in range(len(s)):
            if s[i] != s[j]:
                continue
            j = max(j, i + 1)
            while j < len(s) and s[j] == s[i]:
                j += 1
            answer += sum(cost[i:j]) - max(cost[i:j])
            if j >= len(s):
                break
                   
        return answer