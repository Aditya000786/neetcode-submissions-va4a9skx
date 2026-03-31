from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0: return False
        @lru_cache(None)
        def dfs(ind, left):
            if left == 0: return True
            for i in range(ind, len(nums)):
                diff = left - nums[i]
                if diff >= 0:
                    if dfs(i+1, diff):
                        print("i+1", i+1, diff)
                        return True
            return False

        return dfs(0, int(sum(nums)//2))