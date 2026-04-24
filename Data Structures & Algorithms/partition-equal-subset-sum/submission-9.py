from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        
        @lru_cache(None)
        def dfs(ind, sub_sum):
            if ind >= len(nums): return False
            if sub_sum > target: return False
            if sub_sum == target: return True
            return dfs(ind+1, sub_sum+nums[ind]) or dfs(ind+1, sub_sum)
        
        return dfs(0, 0)