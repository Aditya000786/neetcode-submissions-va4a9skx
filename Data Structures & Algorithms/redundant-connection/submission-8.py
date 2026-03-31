from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        cycleStart = -1
        visited = set()
        cycle = set()
        def dfs(node, par):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh == par: continue
                if dfs(neigh, node):
                    if cycleStart == node:
                        cycle.add(node)
                        cycleStart = -1
                    if cycleStart != -1:
                        cycle.add(node)
                    return True
            return False
        dfs(1,-1)
        print("cycle", cycle)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        
        return []
