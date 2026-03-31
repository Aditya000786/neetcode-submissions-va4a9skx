class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, cost in flights:
            graph[s].append((d, cost))
        k+=1
        heap = [(0, src, k)]
        # print(graph)
        while heap:
            cost, s, c_k = heapq.heappop(heap)
            # print("||", cost, s, c_k )
            if c_k>=0:
                if s == dst:
                    return cost
                for neigh, neigh_cost in graph[s]:
                    heapq.heappush(heap, (cost+neigh_cost, neigh, c_k-1))
        return -1