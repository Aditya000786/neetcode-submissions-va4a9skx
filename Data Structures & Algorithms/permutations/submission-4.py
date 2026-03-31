class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        res = []
        for ind in range(len(nums)):
            curr_num = nums[ind]
            curr_perm = self.permute(nums[0:ind] + nums[ind+1: len(nums)])
            for perm in curr_perm:
                res.append([curr_num] + perm)
        return res