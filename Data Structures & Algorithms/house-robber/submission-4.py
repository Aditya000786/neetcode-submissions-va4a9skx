from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache()
        def dp(ind):
            if ind>=len(nums):
                return 0
            return max(nums[ind] + dp(ind+2), dp(ind+1))
        return max(dp(0), dp(1))