class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_pointer, end_pointer = 0, 0
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        res = 0
        count = 0
        while start_pointer< len(start) and end_pointer<len(end):
            if start[start_pointer]<end[end_pointer]:
                count+=1
                res = max(res, count)
                start_pointer+=1
            else:
                count-=1
                end_pointer+=1
        return res