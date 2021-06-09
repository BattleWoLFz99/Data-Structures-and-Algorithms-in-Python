class Solution:
    def sortIntegers(self, A):
        if not A:
            return A

        temp = [0] * len(A)
        self.merge_sort(A, 0, len(A) - 1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return

        # Left. Right. Merge
        self.merge_sort(A, start, (start + end) // 2, temp)
        self.merge_sort(A, (start + end) // 2 + 1, end, temp)
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):
        middle = (start + end) // 2
        left_index = start
        right_index = middle + 1
        index = left_index

        while left_index <= middle and right_index <= end:
            if A[left_index] < A[right_index]:
                temp[index] = A[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = A[right_index]
                index += 1
                right_index += 1

        # Similar to merge two linked list
        while left_index <= middle:
            temp[index] = A[left_index]
            index += 1
            left_index += 1

        while right_index <= end:
            temp[index] = A[right_index]
            index += 1
            right_index += 1

        for i in range(start, end + 1):
            A[i] = temp[i]

s = Solution()
A = [32, 423, 423, 4, 235, 53, 1, 23, 4]
s.sortIntergers(A)
print(A)