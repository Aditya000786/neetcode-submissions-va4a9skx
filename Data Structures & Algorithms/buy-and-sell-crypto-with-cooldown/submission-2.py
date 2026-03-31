class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        def dfs(ind, buying):
            if ind>=N:
                return 0
            cooldown = dfs(ind+1, buying)
            if buying:
                buy = dfs(ind+1, not buying) - prices[ind]
                ans = max(buy, cooldown)
            else:
                sell = dfs(ind+2, not buying) + prices[ind]
                ans = max(sell, cooldown)
            return ans
        ans = dfs(0, True)
        return ans