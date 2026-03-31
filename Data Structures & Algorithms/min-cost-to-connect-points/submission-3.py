import heapq

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def merge(self, x, y):
        if self.find(x)==self.find(y): return
        if self.rank[self.find(x)] < self.rank[self.find(y)]:
            self.parent[self.find(x)] = self.find(y)
        else:
            self.parent[self.find(y)] = self.find(x)
            self.rank[self.find(x)] += 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        dsu = DSU(len(points))
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = (abs(points[j][0] - points[i][0]) + 
                        abs(points[j][1] - points[i][1]))
                heap.append((dist, i, j))
        heapq.heapify(heap)
        ans = 0
        edges = []
        while heap:
            dist, src, dest = heapq.heappop(heap)
            if dsu.find(src) == dsu.find(dest): continue
            dsu.merge(src, dest)
            ans += dist
            edges.append((points[src], points[dest]))
            # if len(edges)+1 == len(points):
            #     break
        # print(visited)
        print("edges", edges)
        return ans