class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(ind):
            if ind == len(nums):
                res.append(curr.copy())
            else:
                dfs(ind+1)
                curr.append(nums[ind])
                dfs(ind+1)
                curr.pop()
        dfs(0)
        return res