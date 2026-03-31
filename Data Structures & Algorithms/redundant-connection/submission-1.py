class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        count = 0
        visited = set()
        graph = defaultdict(list)
        start_of_cycle = None
        n = len(edges)
        pre = [None]*(n+1)
        post = [None]*(n+1)
        cycle_start, cycle_end = None, None
        
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        def dfs(node, prev):
            nonlocal count, start_of_cycle, cycle_start, cycle_end
            if node in visited:
                cycle_end = count
                cycle_start = pre[node]
                return False
            count+=1
            pre[node] = count
            visited.add(node)
            for neigh in graph[node]:
                if neigh!=prev:
                    if not dfs(neigh, node):
                        return False
            count+=1
            post[node] = count
            return True
        dfs(1, None)
        nodes_in_cycle = set()
        for i in range(1, n+1):
            if pre[i] and not post[i]:
                if pre[i]>=cycle_start:
                    nodes_in_cycle.add(i)
        for src, dest in edges[::-1]:
            if src in nodes_in_cycle and dest in nodes_in_cycle:
                return [src, dest]

