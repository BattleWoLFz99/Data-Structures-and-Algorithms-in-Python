class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        range_total = 1
        while reader.get(range_total - 1) < target:
            range_total *= 2

        # start, end = range_total // 2, range_total - 1
        start, end = 0, range_total - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            elif reader.get(mid) == target:
                end = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1