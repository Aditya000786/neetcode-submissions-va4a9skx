from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        que = deque([])
        ans = []
        for i in range(len(nums)):
            if que and i - que[0] + 1>k:
                que.popleft()

            while que and nums[i] > nums[que[-1]]:
                que.pop()

            que.append(i)

            if i >= k-1:
                ans.append(nums[que[0]])
        return ans