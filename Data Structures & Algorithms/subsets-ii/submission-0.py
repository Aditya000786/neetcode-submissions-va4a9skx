class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(curr_elems, ind):
            if ind == len(nums):
                res.append(curr_elems.copy())
                return
            curr_elems.append(nums[ind])
            dfs(curr_elems, ind+1)
            curr_elems.pop()
            while (ind+1)<len(nums) and nums[ind+1] == nums[ind]:
                ind+=1
            dfs(curr_elems, ind+1)
        dfs([], 0)
        return res