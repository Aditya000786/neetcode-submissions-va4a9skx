class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        postOrder = []
        visited = set()
        done = set()
        graph = defaultdict(list)
        for src, des in prerequisites:
            graph[src].append(des)
        print(graph)

        def dfs(node):
            if node in done: return True
            if node in visited:
                return False
            visited.add(node)

            for pre in graph[node]:
                if not dfs(pre):
                    return False

            graph[node] = []
            postOrder.append(node)
            visited.remove(node)
            done.add(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return []
        return postOrder