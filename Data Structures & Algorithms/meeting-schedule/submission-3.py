"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        if not intervals: return True
        prevEnd = -1
        for i in range(len(intervals)):
            if prevEnd>intervals[i].start:
                return False
            prevEnd = intervals[i].end
        return True
