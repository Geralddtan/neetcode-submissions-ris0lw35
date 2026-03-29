class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        newIntervalStart, newIntervalEnd = intervals[0]

        for index, interval in enumerate(intervals[1:]):
            start, end = interval
            if start > newIntervalEnd:
                res.append([newIntervalStart, newIntervalEnd])
                newIntervalStart, newIntervalEnd = start, end
            elif start <= newIntervalEnd and end > newIntervalEnd:
                newIntervalStart = min(start, newIntervalStart)
                newIntervalEnd = max(end, newIntervalEnd)
            else:
                continue
        res.append([newIntervalStart, newIntervalEnd])
        
        return res

