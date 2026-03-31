from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"start: {self.start} end: {self.end}"

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])
        print("start", start)
        print("end", end)
        count = 0
        ans = 0
        curr_end = 0
        curr_start = 0
        while curr_end < len(end) and curr_start<len(start):
            if end[curr_end] > start[curr_start]:
                count += 1
                curr_start += 1
            else:
                count -= 1
                curr_end += 1
            ans = max(ans, count)
        return ans