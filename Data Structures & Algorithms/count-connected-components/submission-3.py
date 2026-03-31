class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for neigh in graph[node]:
                if neigh == prev: continue
                dfs(neigh, node)
            return True
        ans=0
        for node in range(n):
            if dfs(node, -1):
                ans+=1
        return ans
