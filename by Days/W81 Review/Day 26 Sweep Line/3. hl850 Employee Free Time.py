"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employeeFreeTime(self, schedule):
        import heapq
        heap, results = [], []
        for employee in schedule:
            for i in range(0, len(employee), 2):
                heapq.heappush(heap, (employee[i], -1))
                heapq.heappush(heap, (employee[i + 1], 1))

        count = 0
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heap[0]
            count += left[1]
            if left[1] == 1 and right[1] == -1 and count == 0:
                results.append(Interval(left[0], right[0]))

        return results