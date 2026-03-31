class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()
        cyclestart = -1
        cycle = set()

        def dfs(node, par):
            nonlocal cyclestart
            if node in visited:
                if cyclestart == -1:
                    cyclestart = node
                    return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh == par: continue
                if dfs(neigh, node):
                    if cyclestart != -1:
                        cycle.add(node)
                    if cyclestart == node:
                        cyclestart = -1
                    return True
            return False
            
        dfs(1, None)
        print("cycle", cycle)
        for x, y in edges[::-1]:
            if x in cycle and y in cycle:
                return [x,y]


                