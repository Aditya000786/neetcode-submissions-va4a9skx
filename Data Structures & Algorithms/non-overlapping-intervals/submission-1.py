class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        ind = 0
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        while ind < len(intervals):
            start, end  = intervals[ind][0], intervals[ind][1]
            ind+=1
            overlapping_intervals = []
            while ind<len(intervals) and intervals[ind][0]<end:
                res+=1
                ind+=1
        return res