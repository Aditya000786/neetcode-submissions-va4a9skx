class Solution:
    def rob(self, nums: List[int]) -> int:
        max_arr = [0] * len(nums)
        max_arr[0] = nums[0]
        for i in range(1, len(nums)):
            max_arr[i] = max(max_arr[i-1], max_arr[i-2] + nums[i])
        return max_arr[-1]