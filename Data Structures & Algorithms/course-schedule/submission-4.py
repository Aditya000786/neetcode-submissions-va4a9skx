class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False for i in range(numCourses)]
        graph = defaultdict(list)
        def dfs(node):
            if visited[node]:
                return False
            visited[node] = True
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            visited[node] = False
            return True
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True