class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = nums[0]
        ind = 0
        while ind<len(nums):
            currJump = nums[ind]
            maxJump = max(currJump, maxJump-1)
            ind+=1
            if maxJump==0:
                break
        return True if ind==len(nums) else False