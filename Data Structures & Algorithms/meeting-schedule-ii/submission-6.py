"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        heap = []
        heapq.heapify(heap)
        intervals = sorted(intervals, key=lambda x:x.start)
        # print(sorted_intervals)
        heapq.heappush(heap, intervals[0].end)
        # print(heap)
        i = 1
        ans = 1
        while True:
            if i == len(intervals):
                break
            while heap:
                poped = heapq.heappop(heap)
                if poped>intervals[i].start:
                    heapq.heappush(heap, poped)
                    break
            heapq.heappush(heap, intervals[i].end)
            ans = max(ans, len(heap))
            i+=1
        return ans