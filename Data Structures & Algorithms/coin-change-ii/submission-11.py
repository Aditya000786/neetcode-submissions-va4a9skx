from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(ind, curr_amount):
            if curr_amount == amount: 
                return 1
            if ind>=len(coins) or curr_amount + coins[ind] > amount:
                return 0
            ans = 0
            ans += dfs(ind, curr_amount + coins[ind])
            ans += dfs(ind+1, curr_amount)
            return ans

        coins.sort()
        return dfs(0, 0)
