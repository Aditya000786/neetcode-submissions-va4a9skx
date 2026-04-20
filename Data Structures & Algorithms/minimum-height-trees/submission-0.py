class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        def bfs(root):
            que = deque([root])
            visited = set()
            length = 0
            while que:
                length+=1
                for i in range(len(que)):
                    node = que.popleft()
                    if node in visited: continue
                    visited.add(node)
                    for neigh in graph[node]:
                        if neigh in visited: continue
                        que.append(neigh)
            return length
        ans = []
        length = 0
        curr_min = float('inf')
        for root in range(n):
            length = bfs(root)
            if length<curr_min:
                ans = [root]
                curr_min = length
            elif length == curr_min:
                ans.append(root)
        return ans