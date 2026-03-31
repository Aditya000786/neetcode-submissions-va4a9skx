from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache()
        def dfs(ind):
            if ind>=len(cost):
                return 0
            return cost[ind] + min(dfs(ind+1),dfs(ind+2))
        return min(dfs(0), dfs(1))