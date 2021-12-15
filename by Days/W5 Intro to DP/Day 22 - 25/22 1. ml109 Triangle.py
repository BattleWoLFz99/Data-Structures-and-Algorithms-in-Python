# V1 DFS TLE O(2^n)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        self.mininum = sys.maxsize
        self.traverse(triangle, 0, 0, 0)
        return self.mininum

    def traverse(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.mininum = min(path_sum, self.mininum)
            return

        self.traverse(triangle, x + 1, y, path_sum + triangle[x][y])
        self.traverse(triangle, x + 1, y + 1, path_sum + triangle[x][y])


# V2 DQ TLE O(2^n)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        return self.divide_conquer(triangle, 0, 0)

    def divide_conquer(self, triangle, x, y):
        if x == len(triangle):
            return 0

        left = self.divide_conquer(triangle, x + 1, y)
        right = self.divide_conquer(triangle, x + 1, y + 1)

        return min(left, right) + triangle[x][y]



# Memoization Search (no r), intro to DP

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        return self.divide_conquer(triangle, 0, 0, {})

    # 函数返回从 x, y 出发，走到最底层的最短路径值
    # memo 中 key 为二元组 (x, y)
    # meno 中 value 为从 x, y 走到最底层的最短路径值
    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0

        # 如果找过了，就不要再找了，直接把之前找到的值返回
        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        
        # 在 return 之前先把这次找到的最短路径值记录下来
        # 避免之后重复搜索
        memo[(x, y)] = min(left, right) + triangle[x][y]

        return memo[(x, y)]

# Deeper, go Day 23