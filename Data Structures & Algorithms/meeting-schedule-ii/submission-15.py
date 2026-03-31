"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key = lambda x: x.start)
        # conflicts = 0
        # prevEnd = -1
        # ind = 0
        # while ind < len(intervals):
        #     curr = intervals[ind]
        #     if prevEnd <= curr.start:
        #         prevEnd = curr.end
        #     else:
        #         prevEnd = min(prevEnd, curr.end)
        #         conflicts+=1
        #     ind+=1  
        # print("intervals", [(x.start, x.end) for x in intervals])
        # return conflicts + min(1, len(intervals))

        end = sorted([x.end for x in intervals])
        start = sorted([x.start for x in intervals])
        end_pointer, start_pointer = 0, 0
        ans = 0
        while start_pointer < len(intervals):
            while start[start_pointer]>=end[end_pointer]:
                end_pointer += 1
            ans = max(ans, start_pointer-end_pointer+1)
            start_pointer+=1
        return ans




