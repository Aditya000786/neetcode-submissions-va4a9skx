class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = curr
        for num in nums[1:]:
            curr = max(num, curr+num)
            if curr>ans:
                ans = curr
        return ans