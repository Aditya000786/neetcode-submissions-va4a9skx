class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visiting = set()
        visited = set()

        print("graph", graph)
        
        def dfs(node):
            if node in visiting: return False
            if node in visited: return True
            visiting.add(node)

            for neigh in graph[node]:
                if not dfs(neigh): return False

            visiting.remove(node)
            visited.add(node)
            return True


        for node in range(numCourses):
            if node in visited: continue
            if not dfs(node): return False
        return True
