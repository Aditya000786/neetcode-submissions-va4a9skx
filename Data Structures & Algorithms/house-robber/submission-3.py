class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        ans = [None] * N
        ans.append(0)
        ans[-2] = nums[-1]
        for i in range(N-2, -1, -1):
            ans[i] = max(ans[i+2] + nums[i], ans[i+1])
        return ans[0]