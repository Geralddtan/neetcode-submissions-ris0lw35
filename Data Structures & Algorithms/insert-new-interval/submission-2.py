class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for index, interval in enumerate(intervals):
            start, end = interval
            if end < newInterval[0]:
                res.append(interval)
            elif start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[index:]
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]

        res.append(newInterval)
        return res
