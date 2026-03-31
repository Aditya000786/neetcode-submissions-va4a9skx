class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * (n)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return

        if self.rank[x_root]<self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root]+=1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for src, dest in edges:
            dsu.merge(src, dest)
        count = 0
        visited = set()
        for i in range(n):
            i_root = dsu.find(i)
            if i_root not in visited:
                visited.add(i_root)
                count+=1
        return count

        