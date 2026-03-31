class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(ind):
            if ind >= len(nums): return 0
            curr = nums[ind]
            ans = 0
            for i in range(ind+1, len(nums)):
                if nums[i]>curr:
                    ans = max(ans, dfs(i))
            return ans + 1
        return max(dfs(i) for i in range(len(nums)))