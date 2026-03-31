from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(ind, state, is_bought = False):
            if ind >= len(prices): return 0
            if state == "N":
                sell_value = dfs(ind+1, "S", is_bought) if is_bought else 0
                skip_value = dfs(ind+1, "N", is_bought)
                buy_value = dfs(ind+1, "B", is_bought)
                ans = max(buy_value, skip_value, sell_value)
            elif state == "B":
                skip_value = dfs(ind+1, "N", True)
                sell_value = dfs(ind+1, "S", True)
                ans = max(sell_value, skip_value) - prices[ind]
            elif state == "S":
                skip_value = dfs(ind+1, "N", False) 
                ans = skip_value + prices[ind]
            return ans
        return max(dfs(0, "B"), dfs(0, "N"))