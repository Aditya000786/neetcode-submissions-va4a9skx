from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def dfs(ind):
            if ind == len(s):
                return 1
            ans = 0
            if s[ind] == "0": return 0
            for i in range(ind, len(s)):
                if 1<=int(s[ind:i+1])<=26:
                    ans += dfs(i+1)
            return ans
        ans = dfs(0)
        return ans