from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_s = max(len(w) for w in wordDict)
        wordDict = set(wordDict)
        @lru_cache(None)
        def dfs(ind):
            if ind>=len(s): return True
            for i in range(ind+1, min(len(s), ind+max_s)+1):
                if s[ind:i] in wordDict and dfs(i):
                    return True
            return False
        return dfs(0)