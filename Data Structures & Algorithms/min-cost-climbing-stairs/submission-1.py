class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        ans = [None] * (N)
        ans[-1] = cost[-1]
        ans[-2] = cost[-2]
        for i in range(N-3, -1, -1):
            ans[i] = min(ans[i+1], ans[i+2]) + cost[i]
        return min(ans[0], ans[1])
        cost.append(0)
        def dfs(ind: int) -> int:
            if ind not in cache:
                cache[ind] = min(dfs(ind-1)+cost[ind], dfs(ind-2)+cost[ind])     
            return cache[ind]
        return dfs(len(cost)-1)