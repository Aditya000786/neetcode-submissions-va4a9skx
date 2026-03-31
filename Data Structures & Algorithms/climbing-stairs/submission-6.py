from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache()
        def rec(step):
            if step<=1: return 1
            return rec(step-1) + rec(step-2)
        # return rec(n)
        a,b = 1, 2
        for i in range(n-1, 0, -1):
            a,b = b, a+b
        return a