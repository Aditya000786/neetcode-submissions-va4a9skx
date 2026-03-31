from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)

        for src in graph.keys():
            graph[src].sort()
        
        used_tickets = 0
        ans = []
        def dfs(node):
            nonlocal used_tickets
            neighs = graph[node]
            ans.append(node)

            ind = 0
            while ind < len(neighs):
                neigh = graph[node].pop(ind)
                used_tickets+=1
                is_valid = dfs(neigh)
                if not is_valid:
                    used_tickets-=1
                    graph[node].insert(ind, neigh)
                    ind+=1

            if used_tickets == len(tickets):
                return True
            else:
                ans.pop()
                return False



            # for ind in range(len(neighs)):
            #     neigh = graph[node].pop(ind)
            #     used_tickets+=1
            #     is_valid = dfs(neigh)
            #     if not is_valid:
            #         used_tickets-=1
            #         graph[node].insert(ind, neigh)

            
        dfs("JFK")
        return ans
