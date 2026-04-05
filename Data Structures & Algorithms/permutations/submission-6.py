class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def backtrack(nums):
            if len(nums) == 1:
                ans.append(curr+nums)

            for i in range(len(nums)):
                curr.append(nums[i])
                backtrack(nums[:i] + nums[i+1:])
                curr.pop()

        backtrack(nums)
        return ans