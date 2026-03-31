from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache
        def dfs(ind):
            if ind == len(nums): return 0
            ans = 0
            for j in range(ind, len(nums)):
                if nums[j]>nums[ind]:
                    ans = max(ans, dfs(j))
            return ans + 1
        return max(dfs(i) for i in range(len(nums)))