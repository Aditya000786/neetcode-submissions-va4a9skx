class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True

            visited.add(node)

            for neigh in graph[node]:
                if neigh == par: continue
                if dfs(neigh, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1,-1)
        print("cycle",cycle)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        
        return []
