class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {coin: 1 for coin in coins}
        cache[0] = 0
        def sub(amount):
            if amount<0:
                return float('infinity')
            if amount in cache:
                return cache[amount]
            res = float('infinity')
            for coin in coins:
                res = min(res, sub(amount - coin))
            cache[amount] = res+1
            return cache[amount]
        ans = sub(amount)
        return -1 if ans == float('infinity') else ans