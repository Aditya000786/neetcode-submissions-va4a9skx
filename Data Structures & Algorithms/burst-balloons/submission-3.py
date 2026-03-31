class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def backtrack(nums):
            if len(nums) == 0: return 0
            ans = 0
            for i in range(len(nums)):
                left, right = 1, 1
                if i-1 >=0:
                    left = nums[i-1]
                if i+1 < len(nums):
                    right = nums[i+1]
                temp = left * nums[i] * right
                temp += backtrack(nums[:i]+ nums[i+1:])
                ans = max(ans, temp)
            return ans
        return backtrack(nums)