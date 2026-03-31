class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1), len(w2))
            if w1[:minlen] == w2[:minlen] and len(w1)>len(w2):
                return ""
            for i in range(minlen):
                if w1[i]!=w2[i]:
                    adj[w1[i]].add(w2[i])
                    break
        visit = {}
        postorder = []
        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node] = True
            for neigh in adj[node]:
                if dfs(neigh):
                   return True
            visit[node] = False 
            postorder.append(node)

        for c in adj.keys():
            if dfs(c):
                return ""
        return "".join(postorder[::-1])
        print(adj)