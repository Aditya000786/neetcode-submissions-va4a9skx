class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def dfs(l, r):
            if l>r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            else:
                cache[(l,r)] = 0
                for i in range(l, r+1):
                    ans = nums[l-1] * nums[i] * nums[r+1]
                    ans += dfs(l,i-1)
                    ans += dfs(i+1, r)
                    cache[(l,r)] = max(cache[(l,r)], ans)
                return cache[(l,r)]
        return dfs(1, len(nums)-2)