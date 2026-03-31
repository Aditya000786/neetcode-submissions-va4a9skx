import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        org_queries = queries.copy()
        queries.sort()
        intervals.sort(key = lambda x: x[0])
        ind = 0
        interval_pointer = 0
        min_heap = []
        res = {}
        while ind<len(queries):
            while (interval_pointer < len(intervals) 
            and intervals[interval_pointer][0]<=queries[ind]):
                heapq.heappush(min_heap, 
                (intervals[interval_pointer][1]-intervals[interval_pointer][0],
                intervals[interval_pointer][0],
                intervals[interval_pointer][1]
                ))
                interval_pointer+=1

            while min_heap and min_heap[0][2]<queries[ind]:
                heapq.heappop(min_heap)
            if min_heap:
                res[queries[ind]] = min_heap[0][0]+1
            else:
                res[queries[ind]] = -1
            ind+=1
        return [res[q] for q in org_queries]