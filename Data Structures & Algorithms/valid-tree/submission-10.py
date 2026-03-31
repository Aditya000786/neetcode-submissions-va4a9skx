from typing import List
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: return False
        rank_x, rank_y = self.rank[root_x], self.rank[root_y]
        if rank_x > rank_y:
            self.parent[root_y] = root_x
        elif rank_y < rank_x:
            self.parent[root_x] = root_y
        else:
            self.rank[root_x]+=1
            self.parent[root_x] = root_y
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        dsu = DSU(n)
        for x, y in edges:
            if not dsu.union(x, y): return False
        top_level = set()
        for i in range(n):
            top_level.add(dsu.find(i))
        return True if len(top_level) == 1 else False