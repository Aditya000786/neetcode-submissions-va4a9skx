class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []
        def backtrack(open, close):
            if open>n:
                return

            if open == close == n:
                ans.append("".join(curr))
                return

            if open<n:
                curr.append("(")
                backtrack(open+1, close)
                curr.pop()
            if open-close>0:
                curr.append(")")
                backtrack(open, close+1)
                curr.pop()
            return
        backtrack(0,0)
        return ans
