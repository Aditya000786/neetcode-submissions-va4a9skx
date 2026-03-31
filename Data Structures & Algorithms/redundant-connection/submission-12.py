class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh == parent: continue
                if dfs(neigh, node): return True
            visited.remove(node)
            return False

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            visited = set()
            if dfs(x, None):
                return [x,y]
