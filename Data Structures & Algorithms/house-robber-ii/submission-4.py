class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def sub(nums):
            a,b = 0, nums[-1]
            for i in range(len(nums)-2, -1, -1):
                a, b = b, max(nums[i]+a, b)
            return b
        return max(sub(nums[1:]), sub(nums[:-1]))