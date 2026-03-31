class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        num_map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6': "mno", 
        '7':"pqrs", '8':"tuv", '9':"wxyz"}
        ans = []
        curr = []
        def dfs(ind):
            if ind==len(digits):
                ans.append("".join(curr))
                return
            # for i in range(ind, len(digits)):
            vals = num_map[digits[ind]]
            for l in vals:
                curr.append(l)
                dfs(ind+1)
                curr.pop()
        dfs(0)
        return ans