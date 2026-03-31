class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ind = 1
        curr_fuel = nums[0]
        while ind < len(nums):
            if curr_fuel == 0:
                return False
            curr_fuel = max(curr_fuel - 1, nums[ind])
            ind+=1
        return True