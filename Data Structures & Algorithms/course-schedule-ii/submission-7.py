class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        print("numCourses", numCourses)
        ans = []
        graph = defaultdict(list)
        indegree = {node: 0 for node in range(numCourses)}
        for src, dest in prerequisites:
            graph[src].append(dest)
            indegree[dest]+=1
        que = deque([])
        for node in range(numCourses):
            if indegree[node] == 0:
                que.append(node)
        while que:
            for i in range(len(que)):
                node = que.popleft()
                ans.append(node)
                for neigh in graph[node]:
                    indegree[neigh]-=1
                    if indegree[neigh] == 0:
                        que.append(neigh)
        return ans[::-1] if len(ans) == numCourses else []