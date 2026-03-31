from functools import lru_cache

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
        
        @lru_cache(None)
        def dp(left_ind, right_ind):
            print("dp in", left_ind, right_ind)
            ans = 0
            if right_ind - left_ind<=1: 
                print("dp out", left_ind, right_ind, 0)
                return 0
            if right_ind - left_ind == 2:
                print("dp out", left_ind, right_ind, nums[left_ind] * nums[left_ind+1] * nums[right_ind])
                return nums[left_ind] * nums[left_ind+1] * nums[right_ind]

            for i in range(left_ind+1, right_ind):
                left_sub = dp(left_ind, i)
                right_sub = dp(i, right_ind)
                ans = max(ans, left_sub + right_sub + nums[left_ind]*nums[i]*nums[right_ind])

            print("dp out", left_ind, right_ind, ans)
            return ans
        nums = [1] + nums + [1]
        print("nums", nums)
        return dp(0, len(nums)-1)