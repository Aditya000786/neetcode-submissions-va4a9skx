"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        hash_map = {}
        for interval in intervals:
            hash_map[interval.start] = 1 + hash_map.get(interval.start, 0)
            hash_map[interval.end] = -1 + hash_map.get(interval.end, 0)
        curr=0
        ans = 0
        for key in sorted(hash_map.keys()):
            curr += hash_map[key]
            ans = max(ans, curr)
        return ans

