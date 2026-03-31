class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        res = 0
        ind = 1
        while ind<len(prices):
            if prices[ind]<prices[start]:
                start = ind
            res = max(res, prices[ind]-prices[start])
            ind+=1
        return res