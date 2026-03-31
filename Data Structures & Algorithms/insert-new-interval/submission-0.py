class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for ind in range(len(intervals)):
            interval = intervals[ind]
            if newInterval[0] > interval[1]:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                res += intervals[ind:]
                return res
            else:
                newInterval = min(interval[0], newInterval[0]), max(interval[1], newInterval[1])
        res.append(newInterval)
        return res