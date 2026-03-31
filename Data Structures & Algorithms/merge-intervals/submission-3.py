import copy
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        ind = 0
        prev = intervals[0]
        ind = 1
        while ind < len(intervals):
            curr = intervals[ind]

            if prev[1] < curr[0]:
                res.append(prev)
                ind+=1
                prev = curr
            else:
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                ind+=1
        res.append(prev)
        return res
