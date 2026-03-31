class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr_elems, ind, total):
            print(curr_elems, ind)
            if ind>=len(nums) or total>target:
                return
            if total == target:
                res.append(curr_elems.copy())
                return

            dfs(curr_elems + [nums[ind]], ind, total+nums[ind])
            dfs(curr_elems, ind+1, total)

        dfs([nums[0]], 0, nums[0])
        dfs([], 1, 0)
        return res