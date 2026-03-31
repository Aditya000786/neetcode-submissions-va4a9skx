from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i,j):
            if i>=len(s) and j>=len(p): return True
            if i<len(s) and j>=len(p): return False
            if i>=len(s):
                if j<len(p):
                    if j+1 == len(p)-1 and p[j+1]=="*": return True
                    else: return False

            if s[i] == p[j]:
                if j+1<len(p) and p[j+1] == "*":
                    return dfs(i+1, j) or dfs(i+1, j+2) or dfs(i, j+2)
                else:
                    return dfs(i+1, j+1)
            elif p[j] == ".":
                    if j+1<len(p) and p[j+1] == "*":
                        return dfs(i+1, j) or dfs(i+1, j+2) or dfs(i, j+2)
                    else:
                        return dfs(i+1, j+1)
            elif j+1<len(p) and p[j+1] == "*":
                return dfs(i, j+2)
            else:
                return False
        return dfs(0,0)