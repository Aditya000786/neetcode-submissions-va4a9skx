from functools import lru_cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def backtrack(ind):
            if ind >= len(nums)-1: return 0
            ans = float('inf')
            for i in range(ind+1, ind+nums[ind]+1):
                ans = min(ans, backtrack(i))
            return ans + 1
        return backtrack(0)