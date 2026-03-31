class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], sc: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        graph = defaultdict(list)
        for src, dest, price in flights:
            graph[src].append((dest, price))

        dist[sc] = 0
        for i in range(k+1):
            prev = dist.copy()
            for src in graph.keys():
                for dest, price in graph[src]:
                    dist[dest] = min(dist[dest], prev[src] + price)
        
        return dist[dst] if dist[dst] != float('inf') else -1