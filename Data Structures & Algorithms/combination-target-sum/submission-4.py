class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(curr_sum, ind):
            if curr_sum == target:
                ans.append(subset.copy())
                return
            elif ind==len(nums) or curr_sum>target:
                return 
            for i in range(ind, len(nums)):
                subset.append(nums[i])
                dfs(curr_sum+nums[i], i)
                subset.pop()
                # dfs(curr_sum, i+1) 
        dfs(0,0)
        return list(ans)