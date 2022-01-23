class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        # write your code here
        if not A:
            return 0

        temp = [0] * len(A)
        return self.merge_sort(A, temp, 0, len(A) - 1)

    def merge_sort(self, A, temp, start, end):
        if start >= end:
            return 0

        mid = (start + end) // 2
        count = 0
        count += self.merge_sort(A, temp, start, mid)
        count += self.merge_sort(A, temp, mid + 1, end)
        count += self.merge(A, temp, start, mid, end)
        return count

    def merge(self, A, temp, start, mid, end):
        left_index = start
        right_index = mid + 1
        index = start
        count = 0

        while left_index <= mid and right_index <= end:
            # 这里注意是 <=
            if A[left_index] <= A[right_index]:
                temp[index] = A[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = A[right_index]
                index += 1
                right_index += 1
                count += mid - left_index + 1
        while left_index <= mid:
            temp[index] = A[left_index]
            index += 1
            left_index += 1
        while right_index <= end:
            temp[index] = A[right_index]
            index += 1
            right_index += 1
        for i in range(start, end + 1):
            A[i] = temp[i]

        return count
    