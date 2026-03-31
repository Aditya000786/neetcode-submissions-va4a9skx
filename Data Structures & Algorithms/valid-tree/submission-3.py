from typing import List


class Solution:
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [1 for i in range(n)]
            self.comps = n
            
        
        def find(self, k):
            if k!=self.parent[k]:
                self.parent[k] = self.find(self.parent[k])
            return self.parent[k]
        
        def union(self, u, v):
            pu = self.find(u)
            pv = self.find(v)
            if pu == pv:
                return True
            
            self.comps -= 1
            if self.rank[pu] < self.rank[pv]:
                pu, pv  = pv, pu

            self.rank[pu] += 1
            self.parent[pv] = pu
            return True
                
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        dsu = Solution.DSU(n)
        for u, v in edges:
            if not dsu.union(u,v):
                return False
        return dsu.comps==1