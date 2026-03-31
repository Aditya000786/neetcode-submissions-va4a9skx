from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pattern_to_word = defaultdict(list)
        for word in wordList + [beginWord]:
            for ind in range(len(word)):
                pattern = word[:ind] + "*" + word[ind+1:]
                pattern_to_word[pattern].append(word)
        print("pattern_to_word", pattern_to_word)
        que = deque([beginWord])
        visited = set()
        ans = 0
        while que:
            print("que", que, ans)
            for i in range(len(que)):
                word = que.popleft()
                if word in visited: continue
                visited.add(word)
                for ind in range(len(word)):
                    pattern = word[:ind] + "*" + word[ind+1:]
                    for neigh in pattern_to_word[pattern]:
                        if neigh == endWord: return ans + 2
                        if neigh not in visited:
                            que.append(neigh)
            ans+=1
        return 0