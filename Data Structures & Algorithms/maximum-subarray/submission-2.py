class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        ans = nums[0]
        ind = 1
        uptill = nums[0]
        while ind<len(nums):
            if nums[ind]>nums[ind]+uptill:
                uptill = nums[ind]
            else:
                uptill = uptill+nums[ind]

            ans = max(ans, uptill)
            ind+=1
        return ans