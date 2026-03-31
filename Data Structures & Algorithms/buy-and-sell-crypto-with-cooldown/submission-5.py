from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(ind, in_buying):
            if ind>=len(prices): return 0
            if in_buying:
                cooldown = dp(ind+1, in_buying)
                sold = dp(ind+2, False) + prices[ind]
                return max(cooldown, sold)
            else:
                cooldown = dp(ind+1, in_buying)
                bought = dp(ind+1, True) - prices[ind]
                return max(cooldown, bought)
        return dp(0, False)