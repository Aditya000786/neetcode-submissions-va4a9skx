class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        indegree = {i: 0 for i in range(n)}
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            indegree[src] = indegree.get(src, 0) + 1
            indegree[dest] = indegree.get(dest, 0) + 1

        leaf_nodes = deque([])
        for node in range(n):
            if indegree[node] == 1:
                leaf_nodes.append(node)
        
        
        while n>2:
            leaves_count = len(leaf_nodes)
            n -= leaves_count
            for i in range(len(leaf_nodes)):
                node = leaf_nodes.popleft()
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 1:
                        leaf_nodes.append(neigh)
        return list(leaf_nodes)
