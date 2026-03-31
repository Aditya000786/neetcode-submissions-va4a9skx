class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        ans = [None]*N
        ans[0] = True
        visit = set()
        def sub(ind: int):
            if ind>=N or nums[ind]==0 or ind in visit:
                return
            visit.add(ind)
            for i in range(ind+1, min(ind+nums[ind]+1, N)):
                ans[i] = True
                sub(i)
        sub(0)
        return ans[N-1] if ans[N-1] else False