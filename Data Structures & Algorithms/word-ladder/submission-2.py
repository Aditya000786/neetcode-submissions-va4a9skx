from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pattern_to_words = defaultdict(list)
        for word in [beginWord] + wordList:
            ans = []
            for ind in range(len(word)):
                pattern = word[0:ind] + "*" + word[ind+1:]
                pattern_to_words[pattern].append(word)
        adj_list = defaultdict(list)
        for key in pattern_to_words.keys():
            words = pattern_to_words[key]
            if len(words)==1: continue
            for ind in range(len(words)):
                curr_word = words[ind]
                words.pop(ind)
                adj_list[curr_word] += words.copy()
                words.insert(ind, curr_word)

        # print("adj_list", adj_list)
        que = deque([beginWord])
        visited = set()
        level = 1
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node == endWord:
                    return level
                if node in visited: continue
                visited.add(node)
                for neigh in adj_list[node]:
                    que.append(neigh)
            level+=1
        return 0


