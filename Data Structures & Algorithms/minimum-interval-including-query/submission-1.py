import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        queries_s = sorted(queries)

        heap = []
        output = []
        ans = {}
        curr_interval = 0
        for query in queries_s:
            while (curr_interval < len(intervals) and 
                intervals[curr_interval][0] <= query):
                heapq.heappush(heap, ((intervals[curr_interval][1]-intervals[curr_interval][0] + 1), intervals[curr_interval][1]))
                curr_interval+=1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            if heap:
                ans[query] = heap[0][0]
            else:
                ans[query] = -1
        for query in queries:
            output.append(ans[query])
        return output