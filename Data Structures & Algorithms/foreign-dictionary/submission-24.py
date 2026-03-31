from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        indegree = {}
        for i in range(1, len(words)):
            curr_word, prev_word = words[i], words[i-1]
            min_len = min(len(curr_word), len(prev_word))
            if prev_word[:min_len] == curr_word[:min_len] and prev_word > curr_word:
                return ""
            for j in range(min_len):
                prev_char, curr_char = prev_word[j], curr_word[j]
                if prev_char != curr_char:
                    if prev_char in graph[curr_char]: return ""
                    if curr_char not in graph[prev_char]:
                        graph[prev_char].add(curr_char)
                        indegree[curr_char] = indegree.get(curr_char, 0) + 1
                    break
        que = deque([])
        for node in graph.keys():
            if indegree.get(node, 0) == 0:
                que.append(node)
        # print("graph", graph)
        # print("indegree", indegree)
        # print("que", que)
        visited = set()
        cur_path = set()
        res = []
        def dfs(node):
            if node in visited: return True
            if node in cur_path: 
                return False
            cur_path.add(node)

            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            
            res.append(node)
            cur_path.remove(node)
            visited.add(node)
            return True
            

        for node in graph.keys():
            if not dfs(node):
                return ""
        return "".join(res[::-1])