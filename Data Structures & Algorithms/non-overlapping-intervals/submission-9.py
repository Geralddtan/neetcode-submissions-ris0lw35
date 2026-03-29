class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevEnd = intervals[0][1]
        res = 0
        for index, interval in enumerate(intervals[1:]):
            if interval[0] < prevEnd:
                res += 1
                continue
            prevEnd = interval[1]

        return res