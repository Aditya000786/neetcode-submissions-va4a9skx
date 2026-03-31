import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        start = k
        heap = [(0,k)]
        heapq.heapify(heap)
        visited = set()
        graph = defaultdict(list)
        for src, dest, time in times:
            graph[src].append((dest, time))

        ans = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            ans = time
            visited.add(node)
            for neigh, delta in graph[node]:
                heapq.heappush(heap, (delta+time, neigh))
        return ans if len(visited) == n else -1