import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = 0
        graph = defaultdict(list)
        for src, dest, time in times:
            graph[src].append((time, dest))

        visited = set()
        heap = [(0, k)]
        heapq.heapify(heap)
        while heap:
            time, node = heapq.heappop(heap)
            if node not in visited:
                ans = max(ans, time)
                visited.add(node)
                for c_time, c_node in graph[node]:
                    heapq.heappush(heap, (time+c_time, c_node))
        return ans if len(visited) == n else -1