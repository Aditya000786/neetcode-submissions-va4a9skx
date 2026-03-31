from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = 0
        coins.sort()
        @lru_cache(None)
        def dp(left, ind):
            if left == 0:
                return 1
            if ind>=len(coins) or left<0:
                return 0

            ans = 0
            ans += dp(left-coins[ind], ind)
            ans += dp(left, ind+1)
            return ans
        return dp(amount, 0)
        