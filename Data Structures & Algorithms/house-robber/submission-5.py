from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache()
        def dp(ind):
            if ind>=len(nums):
                return 0
            return max(nums[ind] + dp(ind+2), dp(ind+1))
        # return max(dp(0), dp(1))
        if len(nums)==1: return nums[0]
        dp = [-1] * len(nums)
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2])

        for i in range(len(nums)-3,-1,-1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]