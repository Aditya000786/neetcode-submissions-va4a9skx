class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp={}
        # dp = [[None]*n for _ in range(n)]
        # def max_coins(left: int, right: int)
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            ans = 0
            for i in range(l,r+1):
                coins = nums[l - 1] * nums[i] * nums[r+1]
                coins += dfs(l,i-1) + dfs(i+1, r)
                ans = max(ans, coins)
            dp[(l,r)] = ans
            return dp[(l,r)]
        dfs(1,n-2)
        return dp[(1,n-2)]