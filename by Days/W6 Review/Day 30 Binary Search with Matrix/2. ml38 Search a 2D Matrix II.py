# For follow-up, ver 1 based on 1.

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        count = 0
        start, end = 0, m - 1

        for index in range(n):
            count += self.binary_search(matrix, target, index, start, end, count)

        return count

    def binary_search(self, matrix, target, index, start, end, count):
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[index][mid] < target:
                start = mid
            else:
                end = mid

        if matrix[index][start] == target:
            return 1
        if matrix[index][end] == target:
            return 1
        return 0


# O(m+n):
# elif holy shit....

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        x, y = n - 1, 0
        count = 0

        while x >= 0 and y < m:
            if matrix[x][y] == target:
                x -= 1
                y += 1
                count += 1
            elif matrix[x][y] < target:
                y += 1
            else:
                x -= 1

        return count