from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        @lru_cache(None)
        def dfs(l, r):
            if l>r:
                return 0
            ans = 0
            for i in range(l, r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                ans = max(ans, coins)
            return ans
        return dfs(1, len(nums)-2)
