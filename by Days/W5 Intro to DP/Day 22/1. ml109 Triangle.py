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

    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0

        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        
        memo[(x, y)] = min(left, right) + triangle[x][y]

        return memo[(x, y)]

# Deeper, go Day 23