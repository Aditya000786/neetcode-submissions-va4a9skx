import copy
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        graph = defaultdict(list)
        for dest,src in prerequisites:
            # graph[dest].append(src)
            graph[src].append(dest)
        org_graph = copy.deepcopy(graph)
        postOrder = []
        added_in_order = set()
        # postNumber = 0
        def dfs(node):
            if node in visited:
                return False
            if graph[node] == []:
                if node not in added_in_order:
                    postOrder.append(node)
                    added_in_order.add(node)
                return True
            visited.add(node)
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            graph[node] = []
            visited.remove(node)
            postOrder.append(node)
            added_in_order.add(node)
            return True
        
        for node in range(numCourses):
            if graph[node]==[]:
                if org_graph[node] != []:
                    continue
            if not dfs(node):
                return []
        return postOrder[::-1]

