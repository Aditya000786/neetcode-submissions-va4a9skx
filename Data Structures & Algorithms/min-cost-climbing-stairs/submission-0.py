class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {0: cost[0], 1: cost[1]}
        cost.append(0)
        def dfs(ind: int) -> int:
            if ind not in cache:
                cache[ind] = min(dfs(ind-1)+cost[ind], dfs(ind-2)+cost[ind])     
            return cache[ind]
        return dfs(len(cost)-1)