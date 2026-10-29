class DSU:
    def __init__(self, nodes):
        self.par  = [i for i in range(len(nodes)+1)]
        self.rank = [1]*(len(nodes)+1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]


    def merge(self, x, y):
        rank_x = self.rank[x]
        rank_y = self.rank[y]
        par_x = self.find(x)
        par_y = self.find(y)

        if rank_x > rank_y:
            self.par[par_y] = par_x
        elif rank_y < rank_x:
            self.par[par_x] = par_y
        else:
            self.par[par_y] = par_x
            self.rank[par_x] += 1      

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(edges)
        for (x, y) in edges:
            if dsu.find(x) == dsu.find(y):
                return [x,y]
            else:
                dsu.merge(x, y)
        