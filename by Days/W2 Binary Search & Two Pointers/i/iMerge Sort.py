class Solution:
    def sortIntegers(self, A):
        if not A:
            return A

        # temp = [0] * len(A)
        temp = [0 for _ in range(len(A))]
        self.merge_sort(A, temp, 0, len(A) - 1)

    def merge_sort(self, A, temp, start, end):
        if start >= end:
            return

        # Left. Right. Merge
        mid = (start + end) // 2
        self.merge_sort(A, temp, start, mid)
        self.merge_sort(A, temp, mid + 1, end)
        self.merge(A, temp, start, mid, end)

    def merge(self, A, temp, start, mid, end):
        left_index = start
        right_index = mid + 1
        index = left_index

        while left_index <= mid and right_index <= end:
            if A[left_index] < A[right_index]:
                temp[index] = A[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = A[right_index]
                index += 1
                right_index += 1

        # 不可能两边同时剩下，只可能一边剩下
        while left_index <= mid:
            temp[index] = A[left_index]
            index += 1
            left_index += 1

        while right_index <= end:
            temp[index] = A[right_index]
            index += 1
            right_index += 1

        # 更新原数组
        for i in range(start, end + 1):
            A[i] = temp[i]

s = Solution()
A = [32, 423, 423, 4, 235, 53, 1, 23, 4]
s.sortIntegers(A)
print(A)