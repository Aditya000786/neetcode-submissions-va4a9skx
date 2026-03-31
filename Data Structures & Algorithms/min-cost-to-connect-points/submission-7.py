import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                graph[i].append((dist, i, j))
                graph[j].append((dist, j, i))
        src = 0
        cost = 0
        heap = []
        for edge in graph[src]:
            heapq.heappush(heap, edge)

        visited = set()
        visited.add(src)
        while len(visited)!=len(points):
            dist, src, dest = heapq.heappop(heap)
            if dest in visited: continue
            cost+=dist
            visited.add(dest)
            for edge in graph[dest]:
                heapq.heappush(heap, edge)
        return cost