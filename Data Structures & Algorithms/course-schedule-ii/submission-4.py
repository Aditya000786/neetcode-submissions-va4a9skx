from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # indegree = defaultdict(lambda : 0)
        indegree = {}
        que = []
        for src, dest in prerequisites:
            graph[dest].append(src)
            indegree[src] = 1 + indegree.get(src, 0)
        for node in range(numCourses):
            if indegree.get(node,0) == 0:
                que.append(node)
        que = deque(que)
        ans = []
        while que:
            for i in range(len(que)):
                node = que.popleft()
                ans.append(node)
                for neigh in graph[node]:
                    indegree[neigh]-=1
                    if indegree[neigh] == 0:
                        que.append(neigh)
        return ans if len(ans) == numCourses else []