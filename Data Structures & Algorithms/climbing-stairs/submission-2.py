from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache()
        def rec(step):
            if step<=1: return 1
            return rec(step-1) + rec(step-2)
        return rec(n)
        