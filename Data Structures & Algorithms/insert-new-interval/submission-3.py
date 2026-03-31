class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ind = 0
        new_intervals = []
        is_added = False
        while ind<len(intervals):
            curr = intervals[ind]
            if curr[1]<newInterval[0]:
                new_intervals.append(curr)
                ind+=1
            elif curr[0]>newInterval[1]:
                if not is_added:
                    new_intervals.append(newInterval)
                new_intervals.append(curr)
                is_added = True
                ind+=1
            else:
                newInterval[0] = min(curr[0], newInterval[0]) 
                newInterval[1] = max(curr[1], newInterval[1])
                ind+=1
        if not is_added:
            new_intervals.append(newInterval)
        return new_intervals