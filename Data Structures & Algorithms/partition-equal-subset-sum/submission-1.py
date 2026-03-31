from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0: return False
        
        @lru_cache(None)
        def dp(ind, left):
            if left == 0: return True
            ans = False
            for i in range(ind, len(nums)):
                temp = left - nums[i]
                if temp>=0:
                    if dp(i+1, temp):
                        return True
            return False

        return dp(0, int(sum(nums)//2))