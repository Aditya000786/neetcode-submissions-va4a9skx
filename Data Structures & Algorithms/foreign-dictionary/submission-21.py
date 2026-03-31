class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}

        for ind in range(1, len(words)):
            word1, word2 = words[ind-1], words[ind]
            minlen = min(len(word1), len(word2))
            if word1[:minlen] == word2[:minlen] and len(word1)>len(word2):
                return ""
            for ind in range(len(word1)):
                char1, char2 = word1[ind], word2[ind]
                if char1 == char2: continue
                if char1 in graph[char2]: return ""
                graph[char1].add(char2)
                break
        
        # Detect cycle and get order
        ans = ""
        indegree = {}
        for node in graph.keys():
            for dest in graph[node]:
                indegree[dest] = indegree.get(dest,0) + 1

        start = []
        for node in graph.keys():
            if indegree.get(node,0) == 0:
                start.append(node)
        print("graph", graph)
        visited = {}
        res = []
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for neigh in graph.get(node, []):
                if dfs(neigh): return True
            visited[node] = False
            res.append(node)

        for char in graph.keys():
            if dfs(char): return ""
        return "".join(res[::-1])
        # que = deque(start)
        # ans = []
        # while que:
        #     node = que.popleft()
        #     ans.append(node)
        #     for neigh in graph.get(node, []):
        #         indegree[neigh]-=1
        #         if indegree[neigh] == 0:
        #             que.append(neigh)
        
        # return "" if len(ans)!=len(graph.keys()) else "".join(ans)