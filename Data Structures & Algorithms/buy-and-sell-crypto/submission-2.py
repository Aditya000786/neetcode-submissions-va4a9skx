class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        ans = 0
        for i in range(len(prices)):
            if prices[i]<prices[buy]:
                buy = i
            ans = max(ans, prices[i] - prices[buy])
        return ans