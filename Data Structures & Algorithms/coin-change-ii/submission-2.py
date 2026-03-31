class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = 0
        if amount == 0:
            return 1
        cache = {}
        def dfs(ind, cum):
            if (ind, cum) in cache:
                return cache[(ind, cum)]
            ans = 0
            for i in range(ind, len(coins)):
                new_cum = coins[i] + cum
                if new_cum == amount:
                    ans+=1
                    continue
                if new_cum < amount:
                    ans+=dfs(i, new_cum)
            cache[(ind, cum)] = ans
            return ans
        ans = dfs(0, 0)
        return ans
