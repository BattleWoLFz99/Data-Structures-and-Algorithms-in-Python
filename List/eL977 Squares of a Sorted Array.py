def sortedSquaredArray(array):
    # return a new array of the same length
    #sortedArray = [0] * len(A)
    sortedArray = [0 for _ in array]
    for i in range(len(array)):
	    sortedArray[i] = array[i] * array[i]
    sortedArray.sort()
    return sortedArray

# By default, sort() doesn’t require any extra parameters. However, it has two optional parameters:
# reverse – If true, the list is sorted in descending order
# key – function that serves as a key for the sort comparison
# list1.sort(key=sortSecond,reverse=True)  Time Complexity: nlogn

# To reduce time complexity, we need to avoid sorting the output array:
# Two pointers!


def sortedSquaredArray(array):
    sortedArray = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1
    for i in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedArray[i] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedArray[i] = largerValue * largerValue
            largerValueIdx -=1
        
    return sortedArray


