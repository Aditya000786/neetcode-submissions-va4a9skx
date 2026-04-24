from functools import lru_cache

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(ind, used_m, used_n):
            if used_m > m: return float('-inf')
            if used_n > n: return float('-inf')
            ans = 0
            curr_0 = len([s for s in strs[ind] if s == "0"])
            curr_1 = len([s for s in strs[ind] if s == "1"])

            take, skip = 0,0
            if used_m+curr_0 <= m and used_n+curr_1<=n:
                take = 1

            if ind+1<len(strs):
                skip = dfs(ind + 1, used_m, used_n)
                take += dfs(ind+1, used_m+curr_0, used_n+curr_1)

            ans = max(ans, skip, take)
            return ans
        return dfs(0, 0, 0)