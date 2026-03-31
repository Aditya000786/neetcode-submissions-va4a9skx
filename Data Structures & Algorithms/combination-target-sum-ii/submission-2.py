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
            subset.append(candidates[ind])
            dfs(ind+1, tot+candidates[ind])
            subset.pop()
            j= ind+1
            while j<len(candidates) and candidates[j] == candidates[ind]:
                j+=1
            dfs(j, tot)
            # for i in range(ind, len(candidates)):
            #     if i>ind and candidates[i] == candidates[i-1]:
            #         continue
            #     subset.append(candidates[i])
            #     dfs(i+1, tot+candidates[i])
            #     subset.pop()

        dfs(0, 0)
        return ans
