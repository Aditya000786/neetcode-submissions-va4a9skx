class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        ans_perms = []
        perms = self.permute(nums[1:])
        for p in perms:
            for ind in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(ind, nums[0])
                ans_perms.append(p_copy)
        return ans_perms