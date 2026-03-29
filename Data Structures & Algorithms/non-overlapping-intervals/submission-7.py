class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        res = 0
        prevEnd = intervals[0][1]
        for index in range(1, len(intervals)):
            if intervals[index][0] < prevEnd:
                res += 1
            else:
                prevEnd = intervals[index][1]
    
        return res
