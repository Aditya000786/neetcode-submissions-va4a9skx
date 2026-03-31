class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pre = [1]*N
        suf = [1]*N
        for ind in range(N):
            if ind!=0:
                pre[ind] = pre[ind-1]*nums[ind-1]
                suf[N-ind-1] = suf[N-ind]*nums[N-ind]
        ans = []
        for i in range(N):
            ans.append(pre[i]*suf[i])
        return ans