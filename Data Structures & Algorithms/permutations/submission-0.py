class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            ans = []
            for num in nums:
                perms = self.permute([n for n in nums if n!=num])
                for perm in perms:
                    ans.append([num] + perm)
        return ans