class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(ind):
            if ind == len(s): return 1
            if s[ind] == "0": return 0
            ans = dfs(ind+1) 
            if ind+1<len(s) and 1<=int(s[ind: ind+2])<=26:
                ans += dfs(ind+2)
            return ans
        return dfs(0)