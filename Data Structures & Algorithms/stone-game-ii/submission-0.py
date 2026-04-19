from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(alice, ind, m):
            if ind>= len(piles):
                return 0
            res = 0 if alice else float('inf')
            curr_sum = 0
            for X in range(1, 2*m+1):
                if ind+X > len(piles): continue
                curr_sum += piles[ind+X-1]
                if alice:
                    res = max(res, curr_sum + dfs(not alice, ind+X, max(X, m)))
                else:
                    res = min(res, dfs(not alice, ind+X, max(X, m)))
            return res
        return dfs(True, 0, 1)