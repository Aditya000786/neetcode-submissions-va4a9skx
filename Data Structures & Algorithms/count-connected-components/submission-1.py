class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        # print(graph)
        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for neigh in graph[node]:
                if neigh != prev:
                    dfs(neigh,node)
        
        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node, None)
        return count