from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)
        for word in wordList:
            for ind in range(len(word)):
                pattern = word[0:ind] + "*" + word[ind+1:]
                adj_list[pattern].append(word)
        queue = deque([beginWord])
        res = 1
        visited = set()
        while queue:
            for i in range(len(queue)):
                curr_word = queue.popleft()
                visited.add(curr_word)
                if curr_word == endWord:
                    return res
                for ind in range(len(curr_word)):
                    pattern = curr_word[0:ind] + "*" + curr_word[ind+1:]
                    for neigh in adj_list[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)
            res+=1
        return 0