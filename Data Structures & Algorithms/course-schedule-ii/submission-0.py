from typing import List
from collections import defaultdict
class Solution:
    def make_adj_list(self, prerequisites: List[List[int]]):
        adj = defaultdict(list)
        for requisite in prerequisites:
            # adj[requisite[1]].append(requisite[0])
            adj[requisite[0]].append(requisite[1])
        return adj
            
    def topological_ordering(self, numCourses: int, adj_list: dict)->bool:
        def explore(vertex)->bool:
            visited.add(vertex)
            if vertex in recur_stack:
                return True
            recur_stack.add(vertex)
            for neigh in adj_list[vertex]:
                if neigh not in visited:
                    is_cycle = explore(neigh)
                    if is_cycle:
                        return True
                elif neigh in recur_stack:
                    return True
            recur_stack.remove(vertex)
            post_order.append(vertex)
            return False
            
        visited = set()
        recur_stack = set()
        # clock = numCourses
        post_order = []
        for vertex in list(adj_list.keys()):
            if vertex not in visited:
                is_cycle = explore(vertex)
                if is_cycle: 
                    return []
        # return True if len(visited) == numCourses else False
        for i in range(numCourses):
            if i not in visited:
                post_order.append(i)
        return post_order
    
        
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = self.make_adj_list(prerequisites)
        ans = self.topological_ordering(numCourses, adj_list)
        if ans == False:
            return []
        return ans