from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minlen = min(len(word1), len(word2))
            if len(word2)<len(word1) and word2[:minlen] == word1[:minlen]:
                return ""
            for i in range(minlen):
                if word1[i] != word2[i]:
                    graph[word1[i]].add(word2[i])
                    break
        visit = {}
        ans = ""
        def dfs(node):
            nonlocal ans
            if node in visit:
                return visit[node]
            visit[node] = True
            for neighbour in graph[node]:
                if dfs(neighbour):
                    return ""
            visit[node] = False
            ans+=node
        for key in graph.keys():
            if dfs(key):
                return ""
        return ans[::-1]