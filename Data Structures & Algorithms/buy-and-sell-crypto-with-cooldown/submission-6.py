from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def backtrack(is_buying, ind):
            if ind >= len(prices):
                return 0
            cooldown = backtrack(is_buying, ind+1)
            if is_buying == True:
                buy = backtrack(False, ind+1) - prices[ind]
                return max(buy, cooldown)
            else:
                sell = backtrack(True, ind+2) + prices[ind]
                return max(sell, cooldown)
        return backtrack(True, 0)