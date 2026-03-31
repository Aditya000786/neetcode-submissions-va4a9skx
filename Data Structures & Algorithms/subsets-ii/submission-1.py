class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        def backtrack(ind):
            if ind == len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[ind])
            backtrack(ind+1)
            subset.pop()
            j = ind+1
            while j <len(nums) and nums[j]==nums[ind]:
                j+=1
            backtrack(j)
        backtrack(0)
        return ans