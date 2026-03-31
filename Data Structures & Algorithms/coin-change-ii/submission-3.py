from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        @cache
        def dfs(ind, a):
            if a == amount:
                return 1
            if ind == len(coins) or a> amount:
                return 0
            
            use = dfs(ind, a + coins[ind])
            skip = dfs(ind+1, a)
            return use+skip
        return dfs(0, 0)