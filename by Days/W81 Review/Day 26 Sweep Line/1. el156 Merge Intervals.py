# Greedy:
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result


# Scanline:
    def merge(self, intervals):
        boundaries = []
        for interval in intervals:
            boundaries.append((interval.start, -1))
            boundaries.append((interval.end, 1))
        boundaries.sort()

        results, is_match = [], 0
        for boundary in boundaries:
            if is_match == 0:
                left = boundary[0]
            is_match += boundary[1]
            if is_match == 0:
                right = boundary[0]
                results.append(Interval(left, right))

        return results