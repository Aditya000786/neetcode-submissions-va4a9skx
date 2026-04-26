class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dest, time in times:
            graph[src].append((dest, time))

        ans = float('-inf')
        visited = set()
        heap = [(0,k)]
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited: continue
            visited.add(node)
            ans = max(ans, time)
            for neigh, delta in graph[node]:
                if neigh in visited: continue
                heapq.heappush(heap, (time + delta, neigh))
        return ans if len(visited) == n else -1