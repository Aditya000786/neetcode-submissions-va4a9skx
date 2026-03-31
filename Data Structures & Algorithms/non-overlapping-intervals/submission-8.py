import heapq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        prevEnd = prev_end
        ans = 0
        # for start, end in intervals[1:]:
        #     if start >= prevEnd:
        #         prevEnd = end
        #     else:
        #         ans += 1
        #         prevEnd = min(end, prevEnd)
        # return ans

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                prev_end = min(end, prev_end)
                ans+=1
        return ans