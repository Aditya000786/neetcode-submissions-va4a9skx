import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dist = [[float('inf')]*N for i in range(N)]
        ans = 0
        for i in range(N):
            for j in range(i, N):
                temp = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                if temp>0:
                    dist[j][i] = temp
                    dist[i][j] = temp
        # print(dist)
        heap = [(0,0)]
        heapq.heapify(heap)
        visited = set()
        ans = 0
        while heap:
            c_dist, point = heapq.heappop(heap)
            if point not in visited:
                ans += c_dist
                visited.add(point)
                for neigh in range(N):
                    # print(dist)
                    heapq.heappush(heap, (dist[point][neigh], neigh))
        return ans