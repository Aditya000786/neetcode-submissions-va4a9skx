class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, curr = 0, 0
        ans = 0
        while curr < len(prices):
            if prices[curr]<prices[low]:
                low = curr
            ans = max(ans, prices[curr] - prices[low])
            curr+=1
        return ans
