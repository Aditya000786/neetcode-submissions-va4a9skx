from functools import lru_cache
from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def backtrack(ind):
            if ind >= len(nums)-1: return 0
            ans = float('inf')
            for i in range(ind+1, ind+nums[ind]+1):
                ans = min(ans, backtrack(i))
            return ans + 1
        # return backtrack(0)

        que = deque([0])
        stops = 0
        while que:
            next_start = que[-1]
            stops += 1
            for child in range(len(que)):
                curr = que.popleft()
                for i in range(curr+1, min(curr+1+nums[curr], len(nums))):
                    if i >= len(nums)-1:
                        return stops
                    if i>next_start:
                        que.append(i)
        return 0