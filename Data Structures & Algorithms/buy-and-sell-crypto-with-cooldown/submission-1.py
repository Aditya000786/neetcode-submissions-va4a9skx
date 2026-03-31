class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        # mat = [[None for i in range(N)] for i in range(2)]
        cache = {}
        def dfs(ind, buying, profit):
            # print("start", ind, buying , profit)
            if ind>=N:
                return profit
            if (ind, buying, profit) in cache:
                return cache[(ind, buying, profit)]
            if buying:
                opt1 = dfs(ind+1, not buying, profit - prices[ind])
                opt2 = dfs(ind+1, buying, profit)
                ans = max(opt1, opt2)
            else:
                opt1 = dfs(ind+2, not buying, profit + prices[ind])
                opt2 = dfs(ind+1, buying, profit)
                ans = max(opt1, opt2)
            cache[(ind, buying, profit)] = ans
            # print("end", ind, buying , profit, ans)
            return ans
        ans = dfs(0, True, 0)
        # print(cache)
        return ans