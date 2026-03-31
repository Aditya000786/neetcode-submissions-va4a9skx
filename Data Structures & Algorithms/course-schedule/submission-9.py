class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    def find(self, x):
        curr = x
        if curr != self.parent[curr]:
            self.parent[curr] = self.find(self.parent[curr])
        return self.parent[curr]
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: return False
        rank_x, rank_y = self.rank[x], self.rank[y]
        if rank_x < rank_y:
            self.parent[root_x] = root_y
        elif rank_x > rank_y:
            self.parent[root_y] = root_x
        else:
            self.rank[root_x]+=1
            self.parent[root_y] = root_x
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for cour, prereq in prerequisites:
            graph[cour].append(prereq)
        curr_path = set()
        visited = set()
        def dfs(node):
            if node in curr_path:
                return False
            if node in visited:
                return True
            curr_path.add(node)
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            curr_path.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            visited.add(i)
        return True