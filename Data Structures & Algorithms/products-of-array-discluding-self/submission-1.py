class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        for ind in range(1, len(nums)):
            prefix[ind] = prefix[ind-1] * nums[ind-1]

        suffix = [1]*len(nums)
        for ind in range(len(nums)-2,-1,-1):
            suffix[ind] = suffix[ind+1] * nums[ind+1]

        # print("prefix",prefix)
        # print("suffix",suffix)

        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = prefix[i]*suffix[i]
        return ans
