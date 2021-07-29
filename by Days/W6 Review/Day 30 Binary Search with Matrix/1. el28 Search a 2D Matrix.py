class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False

        n, m = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get(matrix, mid) < target:
                start = mid
            else:
                end = mid

        if self.get(matrix, start) == target:
            return True
        if self.get(matrix, end) == target:
            return True
        return False

        
    def get(self, matrix, index):
        x = index // len(matrix[0])
        y = index % len(matrix[0])
        return matrix[x][y]