class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        curr = []
        ans = []
        def dfs(ind, tot):
            if tot == target:
                ans.append(curr.copy())
                return
            if ind>=len(nums) or tot>target:
                return
            curr.append(nums[ind])
            dfs(ind, tot + nums[ind])
            curr.pop()
            next_ind = ind
            while next_ind < len(nums) and nums[next_ind] == nums[ind]:
                next_ind += 1
            dfs(next_ind, tot)
        dfs(0,0)
        return ans