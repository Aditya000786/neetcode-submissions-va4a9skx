from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for _from, to  in tickets:
            adj_list[_from].append(to)
        sorted_adj_list = defaultdict(list)
        for node, neighbours in adj_list.items():
            sorted_adj_list[node] = sorted(neighbours)
        adj_list = sorted_adj_list
        path = ['JFK']
        def dfs(node):
            if len(path) == len(tickets)+1:
                return True
            if not adj_list[node]:
                return False
            temp = list(adj_list[node])
            for i, v in enumerate(temp):
                adj_list[node].pop(i)
                path.append(v)
                if dfs(v): return True
                adj_list[node].insert(i, v)
                path.pop()
            return False
        dfs('JFK')
        return path