from typing import List
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        dist = [[float('inf')]*(k+2) for node in range(n)]
        def make_adj_list():
            for flight in flights:
                adj[flight[0]].append([flight[1], flight[2]])
                
        def dijkstra(start):
            queue = [(0, start, 0)]
            heapify(queue)
            dist[start][0] = 0
            while queue:
                curr_cost, node, stops_taken = heappop(queue)
                if node == dst:
                    return curr_cost
                if stops_taken>k or dist[node][stops_taken]<curr_cost:
                    continue
                for neigh, curr_neigh_cost in adj[node]:
                    if dist[neigh][stops_taken+1] > curr_cost + curr_neigh_cost:
                        dist[neigh][stops_taken+1] = curr_cost + curr_neigh_cost
                        heappush(queue, (dist[neigh][stops_taken+1], neigh, stops_taken+1))
            return -1
                                
        make_adj_list()
        return dijkstra(src)