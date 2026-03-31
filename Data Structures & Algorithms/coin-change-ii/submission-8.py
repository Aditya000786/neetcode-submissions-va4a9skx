from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(ind, curr):
            if curr == amount: return 1
            if curr>amount or ind>=len(coins): return 0
            ans = 0
            
            ans += dfs(ind, curr + coins[ind])
            ans += dfs(ind+1, curr)
            # for i in range(ind, len(coins)):
            #     ans += dfs(i, curr + coins[i])
            return ans

        return dfs(0, 0)