class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open, close, curr):
            if open>=n:
                close_left = n - close
                if close_left>0:
                    res.append(curr + ")"*close_left)
                return

            dfs(open+1, close, curr+"(")
            if open-close>0:
                dfs(open, close+1, curr+")")
        dfs(0,0,"")
        return res