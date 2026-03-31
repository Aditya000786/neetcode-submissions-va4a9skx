import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        endTimes = [-1]
        for i in range(0, len(intervals)):
            if intervals[i].start<endTimes[0]:
                heapq.heappush(endTimes, intervals[i].end)
            else:
                heapq.heappop(endTimes)
                heapq.heappush(endTimes, intervals[i].end)
        return len(endTimes) if len(intervals)>0 else 0