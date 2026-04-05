from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0: return False
        target = sum(nums)//2

        @lru_cache(None)
        def backtrack(ind, total):
            if total == target: return True
            if ind >= len(nums): return False
            return backtrack(ind+1, total+nums[ind]) or backtrack(ind+1, total)
        return backtrack(0, 0)