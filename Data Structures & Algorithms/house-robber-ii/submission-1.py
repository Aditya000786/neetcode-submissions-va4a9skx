class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        last_nums = nums[:n-1]
        first_nums = nums[1:]
        ans = 0
        rob1, rob2 = 0, 0
        for n in first_nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        ans = max(ans, rob2)

        rob1, rob2 = 0, 0
        for n in last_nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        ans = max(ans, rob2)
        return ans