class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0 
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            currStart = intervals[i][0]
            if prevEnd<=currStart:
                prevEnd = intervals[i][1]
            else:
                prevEnd = min(intervals[i][1], prevEnd)
                ans+=1
        return ans