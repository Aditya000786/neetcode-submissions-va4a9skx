class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        curr = []
        def dfs(ind, tot):
            if tot == target:
                ans.append(curr.copy())
                return
            if ind>=len(candidates) or tot>target:
                return
            curr.append(candidates[ind])
            dfs(ind+1, tot+candidates[ind])
            curr.pop()
            skip_ind = ind+1
            while skip_ind< len(candidates) and candidates[ind] == candidates[skip_ind]:
                skip_ind+=1
            dfs(skip_ind, tot)
            return 
        dfs(0,0)
        return ans