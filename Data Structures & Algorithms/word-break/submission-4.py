from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = Counter(wordDict)
        max_limit = max(len(w) for w in wordDict)
        @lru_cache(None)
        def dfs(ind):
            if ind == len(s):
                return True
            for i in range(ind, min(len(s), ind+max_limit)):
                curr = s[ind:i+1]
                if curr in word_dict:
                    if dfs(i+1):
                        return True
            return False

        return dfs(0)