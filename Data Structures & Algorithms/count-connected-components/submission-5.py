class DSU:
    def __init__(self, n):
        self.parent = [n for n in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def find(self, x):
        curr = x
        while curr!=self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    
    def merge(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)
        if x_par==y_par: return
        x_ran = self.rank[x_par]
        y_ran = self.rank[y_par]
        if x_ran>y_ran:
            self.parent[y_par] = x_par
        else:
            self.parent[x_par] = y_par
            self.rank[y_par] += 1

            

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # graph = defaultdict(list)
        # for a, b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)
        d = DSU(n)
        for a,b in edges:
            d.merge(a, b)
        parents = set()
        for i in range(n):
            parents.add(d.find(i))
        return len(parents)
