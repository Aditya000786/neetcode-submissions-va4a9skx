class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_intervals = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] > prev[1]:
                new_intervals.append(prev.copy())
                prev = curr
                i+=1
            else:
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                i+=1
        new_intervals.append(prev)
        return new_intervals