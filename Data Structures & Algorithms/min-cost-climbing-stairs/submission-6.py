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
        
        dp = [None] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
         
        return min(dp[0], dp[1])

