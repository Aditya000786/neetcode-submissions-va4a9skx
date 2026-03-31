class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        # Checks for lexicographically validity
        indegree = {}
        nodes = set()
        for word in words:
            nodes = nodes.union(set(word))
        for j in range(len(words)-1):
            word1 = words[j]
            word2 = words[j+1]
            minLen = min(len(word1), len(word2))

            if len(word2)<len(word1) and word2 == word1[:len(word2)]:
                return ""
            for i in range(minLen):
                if word1[i] != word2[i]:
                    if word1[i] in graph[word2[i]]:
                        return ""
                    if word2[i] not in graph[word1[i]]:
                        indegree[word2[i]] = 1 + indegree.get(word2[i], 0)
                        graph[word1[i]].add(word2[i])
                    # print("indegree", indegree)
                    break
        # Now check for cycle and do topological sort
        que = []
        ans = []
        for node in nodes:
            if indegree.get(node,0) == 0:
                que.append(node)
        que = deque(que)
        
        print("graph", graph)
        print("indegree", indegree)
        print("nodes", nodes)
        print("que", que)
        while que:
            for i in range(len(que)):
                node = que.popleft()
                ans.append(node)
                for neigh in graph[node]:
                    indegree[neigh]-=1
                    if indegree[neigh] == 0:
                        que.append(neigh)
        # print("ans", ans)
        return "".join(ans) if len(ans) == len(nodes) else ""
        # visited = set()
        # ans = []
        # done = set()
        # def dfs(node):
        #     if node in visited:
        #         return False
        #     visited.add(node)

        #     for neigh in graph[node]:
        #         if not dfs(neigh):
        #             return False
            
        #     if node not in done:
        #         done.add(node)
        #         ans.append(node)

        #     visited.remove(node)
        #     return True
        
        # for key in graph.keys():
        #     if not dfs(key): return ""
        # return "".join(ans[::-1])