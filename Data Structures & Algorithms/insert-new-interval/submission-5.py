class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if curr[1]<newInterval[0]:
                res.append(curr)
            elif newInterval[1]<curr[0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                newInterval = min(newInterval[0], curr[0]), max(newInterval[1], curr[1])
        res.append(newInterval)
        return res