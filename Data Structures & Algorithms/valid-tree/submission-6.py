class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = {}
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        def dfs(node, prev):
            if node in parent:
                if prev is not None and parent[node] != prev:
                    return False
                else:
                    return True
            if prev is not None:
                parent[node] = prev
            for neigh in graph[node]:
                if neigh != prev:
                    if not dfs(neigh, node):
                        return False
            return True
        print(graph)
        for node in range(n):
            parent = {}
            if dfs(node, None):
                print(node, parent)
                return True if len(parent.keys()) == n-1 else False
        return False
        