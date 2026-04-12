class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums):
            if len(nums) == 1:
                return [nums]
            else:
                ans = []
                for i in range(len(nums)):
                    curr_num = nums[i]
                    left_nums = nums[:i] + nums[i+1:]
                    rest_perm = backtrack(left_nums)
                    for perm in rest_perm:
                        ans.append([curr_num] + perm)
            return ans
        return backtrack(nums)