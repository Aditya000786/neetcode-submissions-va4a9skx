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
        print(intervals)
        curr_start_index, curr_end_index = 0, 0
        metting_days = 0
        max_days = 0
        while curr_start_index < len(start):
            if start[curr_start_index] >= end[curr_end_index]:
                metting_days-=1
                curr_end_index+=1
            metting_days+=1
            curr_start_index+=1
            
            max_days = max(max_days, metting_days)
        return max_days