from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(ind):
            if ind==len(nums)-1:
                return [nums[-1], -nums[-1]]

            sub = dfs(ind+1)
            ans = []
            for s in sub:
                ans.append(s+nums[ind])
                ans.append(s-nums[ind])
            return ans
        return len([i for i in dfs(0) if i == target])