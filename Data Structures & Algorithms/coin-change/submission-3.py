from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amount):
            if amount == 0: 
                return 0
            if amount<0:
                return -1
            ans = float('inf')
            for coin in coins:
                temp = dfs(amount-coin)
                if temp!=-1:
                    ans = min(ans, 1 + temp)
            return ans if ans!=float('inf') else -1
        ans = dfs(amount)
        return ans