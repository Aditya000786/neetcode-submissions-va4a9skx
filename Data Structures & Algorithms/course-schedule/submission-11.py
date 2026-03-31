class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = {}
        for cour, prereq in prerequisites:
            graph[prereq].append(cour)
            indegree[cour] = 1 + indegree.get(cour, 0)
        
        que = []
        finish = 0
        for curr in range(numCourses):
            if indegree.get(curr, 0) == 0:
                que.append(curr)
        que = deque(que)
        while que:
            node = que.popleft()
            finish += 1
            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    que.append(neigh)
        return finish == numCourses