class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(curr_elems, ind, total):
            # print(curr_elems, ind, total)
            if total == target:
                res.append(curr_elems.copy())
                return
            if ind>=len(candidates) or total>target:
                return

            curr_elems.append(candidates[ind])
            dfs(curr_elems, ind+1, total+candidates[ind])

            curr_elems.pop()
            while ind+1<len(candidates) and candidates[ind+1] == candidates[ind]:
                ind+=1
            dfs(curr_elems, ind+1, total)
        
        dfs([], 0, 0)
        return res