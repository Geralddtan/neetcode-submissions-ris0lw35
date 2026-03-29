class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        for index in range(len(intervals)):
            if index == 0:
                res.append(intervals[index])
            if intervals[index][0] <= res[-1][1]:
                res[-1][1] = max(intervals[index][1], res[-1][1])
            else:
                res.append(intervals[index])
        
        return res
