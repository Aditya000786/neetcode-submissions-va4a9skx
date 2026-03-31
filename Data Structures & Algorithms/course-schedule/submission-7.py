class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for node, pre in prerequisites:
            graph[node].append(pre)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            graph[node] = []
            visited.remove(node)
            return True
            
        for cour in range(numCourses):
            if not dfs(cour):
                return False
        return True