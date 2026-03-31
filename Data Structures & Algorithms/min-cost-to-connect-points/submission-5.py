import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        heap = [(0,0)]
        visited = set()
        ans = 0
        while heap:
            dist, point = heapq.heappop(heap)
            # print("dist", dist, point)
            if point in visited: continue
            visited.add(point)
            ans += dist
            for nd, np in adj[point]:
                if np in visited: continue
                heapq.heappush(heap, [nd, np])
        return ans