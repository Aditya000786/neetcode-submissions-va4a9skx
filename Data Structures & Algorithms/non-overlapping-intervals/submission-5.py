class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda x: x[0])
        prev_end = intervals[0][1]
        ind = 1
        while ind < len(intervals):
            if prev_end <= intervals[ind][0]:
                prev_end = intervals[ind][1]
                ind+=1
            else:
                prev_end = min(prev_end, intervals[ind][1])
                ans+=1
                ind+=1
        return ans
            
