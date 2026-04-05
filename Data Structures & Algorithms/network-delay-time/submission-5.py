import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, target, time in times:
            graph[src].append((time, target))
        heap = [(0,k)]
        heapq.heapify(heap)
        ans = 0
        visited = set()
        while heap:
            time, new_node = heapq.heappop(heap)
            if new_node in visited: continue
            ans = time
            visited.add(new_node)
            for dest_time, dest in graph[new_node]:
                if dest not in visited:
                    heapq.heappush(heap, (time + dest_time, dest))
        return ans if len(visited) == n else -1