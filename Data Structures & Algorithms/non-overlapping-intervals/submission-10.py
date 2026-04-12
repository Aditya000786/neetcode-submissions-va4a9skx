class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart<prevEnd:
                ans+=1
                prevEnd = min(prevEnd, currEnd)
            else:
                prevEnd = currEnd
        return ans