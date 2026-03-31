class Solution:
    def __init__(self):
        self.hash_map = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        if amount<0:
            return -1
        if amount in self.hash_map:
            return self.hash_map[amount]
        
        possible_ans = []
        for coin in coins:
            delta = self.coinChange(coins, amount-coin)
            if delta>=0:
                possible_ans.append(1+delta)
        self.hash_map[amount] = min(possible_ans) if len(possible_ans)>0 else -1
        return self.hash_map[amount]
    