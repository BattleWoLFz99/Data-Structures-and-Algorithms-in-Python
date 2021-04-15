def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """

    for i in range(len(lst)):
        min_index = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]


# Driver code to test above
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    selection_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)