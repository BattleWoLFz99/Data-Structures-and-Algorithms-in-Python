# 这鸟模板是真的难用。。。。是变数很多的模板，所以抽象后缺少很多细节
# 还是喜欢 while 手控唉。。
# 这里 if continue 是变数，if j越界也是变数， j = max(j, i + 1) 是核心

# 三刷： 好吧本来同向双指针就很郁闷唉。。

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if not colors:
            return 0
        
        j, min_time = 0, 0
        n = len(colors)
        for i in range(n):
            if i < n - 1 and colors[i] != colors[i + 1]:
                continue
            if i < j:
                continue
            j = max(i + 1, j)
            while j < n and colors[j] == colors[i]:
                j += 1
            min_time += sum(neededTime[i:j]) - max(neededTime[i:j])
            if j >= n:
                break
                
        return min_time