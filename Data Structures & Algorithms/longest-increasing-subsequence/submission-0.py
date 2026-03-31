from typing import List
class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     lis = [None] * len(nums)
    #     def dfs(ind) -> int:
    #         if ind in lis and lis[ind]:
    #             return lis[ind]
    #         else:
    #             ans = 0
    #             for next_ind in range(ind+1, len(nums)):
    #                 if nums[next_ind]>nums[ind]:
    #                     ans = max(ans, dfs(next_ind))
    #             lis[ind] = ans+1
    #         return lis[ind]
    #     for ind in range(len(nums)):
    #         dfs(ind)
    #     return max(lis)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [float('-inf')] * n
        lis[-1] = 1
        for i in range(n-2, -1, -1):
            ans = 1
            for j in range(i+1, n):
                if nums[j]>nums[i]:
                    ans = max(ans, 1 + lis[j])
            lis[i] = ans
        return max(lis)