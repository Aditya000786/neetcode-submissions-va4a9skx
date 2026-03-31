class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if curr[1] < newInterval[0]:
                new_intervals.append(curr)
            elif curr[0] > newInterval[1]:
                new_intervals.append(newInterval)
                new_intervals += intervals[i:]
                return new_intervals
            else:
                newInterval = min(newInterval[0], curr[0]), max(newInterval[1], curr[1])
        new_intervals.append(newInterval)
        return new_intervals