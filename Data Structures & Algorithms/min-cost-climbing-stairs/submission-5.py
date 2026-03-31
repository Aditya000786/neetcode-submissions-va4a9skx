from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @lru_cache(None)
        def dp(ind):
            if ind >= n:
                return 0
            return min(dp(ind+1), dp(ind+2)) + cost[ind]
        return min(dp(0), dp(1))