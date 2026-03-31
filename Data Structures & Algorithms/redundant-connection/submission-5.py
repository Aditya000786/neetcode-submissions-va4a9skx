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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        print(dsu.parent)
        for nodex, nodey in edges:
            if not dsu.union(nodex, nodey): return [nodex, nodey]