class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        cycle_start = -1
        curr_path = set()
        cycle = set()
        def dfs(node, parent):
            nonlocal cycle_start
            if node in curr_path:
                cycle_start = node
                return True

            curr_path.add(node)
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node): 
                    if node == cycle_start:
                        cycle_start = -1
                        cycle.add(node)
                    if cycle_start !=-1:
                        cycle.add(node)
                    return True
            curr_path.remove(node)
            return False
        dfs(1, None)
        for u, v in edges[::-1]:
            if u in cycle and v in cycle:
                return [u, v]
