class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        for ind in range(1, len(nums)):
            ans[ind] = ans[ind-1] * nums[ind-1]

        suffix = 1
        for ind in range(len(nums)-2,-1,-1):
            suffix *= nums[ind+1]
            ans[ind] = ans[ind]*suffix
        return ans
        