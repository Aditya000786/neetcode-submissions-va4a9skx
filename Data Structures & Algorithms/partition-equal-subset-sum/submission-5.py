class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0:
            return False
        target = sum(nums)//2
        def dp(ind, curr):
            if curr == target:
                return True
            if ind>=len(nums):
                return False
            return dp(ind+1, curr+nums[ind]) or dp(ind+1, curr)
        return dp(0,0)