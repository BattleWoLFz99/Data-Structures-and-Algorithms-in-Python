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

        # Merge two linked list
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




# In-place(educative.io):

def merge_sort(lst):
    """
    Merge sort function
    :param lst: lst of unsorted integers
    """
    if len(lst) > 1:
        mid = len(lst) // 2  # Mid of the list
        left = lst[:mid]  # Dividing the list elements into 2 halves
        right = lst[mid:]

        merge_sort(left)  # Sorting the first half
        merge_sort(right)  # Sorting the second half

        # Initializing index variables
        i = 0    # For the left half
        j = 0    # For the right half
        k = 0    # Related to final array

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was right
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


# Driver code to test the above code
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    merge_sort(lst)

    print("Sorted list is: ", lst)
