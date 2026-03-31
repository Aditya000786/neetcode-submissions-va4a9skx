class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        # Checks for lexicographically validity
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word2)<len(word1) and word2 == word1[:len(word2)]:
                return ""
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if word1[i] in graph[word2[i]]:
                        return ""
                    graph[word1[i]].add(word2[i])
                    break
        # Now check for cycle and do topological sort
        visited = set()
        ans = []
        done = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)

            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            
            if node not in done:
                done.add(node)
                ans.append(node)

            visited.remove(node)
            return True
        
        for key in graph.keys():
            if not dfs(key): return ""
        return "".join(ans[::-1])