"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        remaining = self.getRemaining(intervals)
        res = 1
        while remaining:
            res += 1
            remaining = self.getRemaining(remaining)

        return res

    def getRemaining(self, intervals):
        intervals.sort(key=lambda x: x.start)
        remaining = []
        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < prevEnd:
                remaining.append(intervals[i])
            else:
                prevEnd = intervals[i].end

        return remaining
