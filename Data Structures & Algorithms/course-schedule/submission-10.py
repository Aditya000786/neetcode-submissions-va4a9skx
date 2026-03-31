class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = {}
        for cour, prereq in prerequisites:
            graph[prereq].append(cour)
            indegree[cour] = 1 + indegree.get(cour, 0)
        
        que = []
        completed_cour = set()

        for curr in range(numCourses):
            if indegree.get(curr, 0) == 0:
                completed_cour.add(curr)
                que.append(curr)
        que = deque(que)
        while que:
            node = que.popleft()
            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    completed_cour.add(neigh)
                    que.append(neigh)
        return len(completed_cour) == numCourses