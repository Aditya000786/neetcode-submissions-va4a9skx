class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return True
        rx, ry = self.rank[px], self.rank[py]
        if rx>ry:
            self.parent[py] = px
        elif ry>rx:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[px]+=1
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        for x, y in edges:
            if dsu.union(x,y):
                return [x,y]

        