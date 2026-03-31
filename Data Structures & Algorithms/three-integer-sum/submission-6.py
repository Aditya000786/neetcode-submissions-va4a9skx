class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        ind = 0
        while ind<len(nums)-2:
            left, right = ind+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] + nums[ind] > 0:
                    right-=1
                elif nums[left] + nums[right] + nums[ind]<0:
                    left+=1
                else:
                    ans.append((nums[ind], nums[left], nums[right]))
                    left+=1
                    while left<len(nums) and nums[left] == nums[left-1]:
                        left+=1
            ind+=1
            while ind<len(nums)-2 and nums[ind] == nums[ind-1]:
                ind+=1
        return ans