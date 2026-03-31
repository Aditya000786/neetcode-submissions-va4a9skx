class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, cost in flights:
            graph[s].append((d, cost))
        k+=1
        heap = [(0, src, k)]
        visited = {}
        while heap:
            cost, s, c_k = heapq.heappop(heap)
            if s == dst:
                return cost
            if c_k == 0:
                continue

            if (s, c_k) in visited and visited[(s, c_k)]<=cost:
                continue
            visited[(s, c_k)]=cost 

            for neigh, neigh_cost in graph[s]:
                heapq.heappush(heap, (cost+neigh_cost, neigh, c_k-1))
        return -1