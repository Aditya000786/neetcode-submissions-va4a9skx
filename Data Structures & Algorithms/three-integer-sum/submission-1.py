class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        for f_ind in range(n-2):
            if f_ind>0 and nums[f_ind] == nums[f_ind-1]:
                continue
            left, right = f_ind+1, n-1
            f_val = nums[f_ind]
            while left<right and left<n and right<n:
                if nums[left]+nums[right]+f_val == 0:
                    ans.append([f_val,nums[left],nums[right]])
                    curr_left_val = nums[left]
                    while left<n and nums[left] == curr_left_val:
                        left+=1
                elif nums[left]+nums[right]+f_val > 0:
                    right-=1
                else:
                    left+=1
        return ans
