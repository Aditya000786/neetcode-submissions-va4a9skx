from typing import List
from collections import defaultdict,deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # A valid tree must have exactly n - 1 edges
        adj=defaultdict(list)
        visited = set()
        post_ordering = {}
        pre_ordering = {}
        clock = 0
        is_cycle = False
        
        def make_adj_list()->None:
            for edge in edges:
                adj[edge[0]].append(edge[1])
                adj[edge[1]].append(edge[0])
                
        def explore(vertex, prev) -> None:
            nonlocal is_cycle
            visited.add(vertex)
            for neigh in adj[vertex]:
                if neigh in visited and neigh!=prev:
                    is_cycle = True
                    return
                if neigh not in visited:
                    explore(neigh, vertex)
            return False
                        
            
        def dfs(vertex) -> None:
            visited.add(vertex)
            if explore(vertex, -1):
                return False
            if len(visited)!=n:
                return False
            return True
                        
        
        make_adj_list()
        return dfs(0)