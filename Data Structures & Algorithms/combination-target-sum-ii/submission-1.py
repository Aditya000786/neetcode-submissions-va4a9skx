class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        candidates.sort()

        def dfs(ind, tot):
            if tot == target:
                ans.append(subset.copy())
                return

            if tot>target or ind == len(candidates):
                return

            for i in range(ind, len(candidates)):
                if i>ind and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                dfs(i+1, tot+candidates[i])
                subset.pop()

        dfs(0, 0)
        return ans
