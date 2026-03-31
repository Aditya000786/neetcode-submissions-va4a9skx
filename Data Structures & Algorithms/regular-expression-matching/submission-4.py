class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ROWS, COLS = len(s), len(p)
        dp = [[None]*COLS for i in range(ROWS)]
        print(ROWS, COLS)
        def dfs(i, j):
            if i == ROWS and j == COLS:
                print("start ind", i, j, "True")
                return True
            elif j == COLS:
                print("start ind", i, j, "False")
                return False
            elif i == ROWS:
                if p[j]=="*" or (j+1<COLS and p[j+1]=="*"):
                    return dfs(i, j+1)
                else:
                    return False
            if dp[i][j] is not None:
                return dp[i][j]
            cs = s[i]
            cp = p[j]
            print("start val", cs, cp, i, j)
            if cp==cs:
                ans = dfs(i+1, j+1)
                if not ans and j+1<COLS and p[j+1]=="*":
                    dp[i][j] = dfs(i, j+1)
                else:
                    dp[i][j] = ans

            elif cp == ".":
                dp[i][j] = dfs(i+1, j+1)
            elif cp == "*":
                skip = dfs(i, j+1)
                if skip:
                    dp[i][j] = True
                else:
                    prev = p[j-1]
                    if prev == "." or prev==cs:
                        use = dfs(i+1, j+1) or dfs(i+1, j)
                        dp[i][j] = use
                    else:
                        dp[i][j] = False
            else:
                if j+1<COLS and p[j+1]=="*":
                    dp[i][j] = dfs(i, j+1)
                else:
                    dp[i][j] = False
            return dp[i][j]
        ans = dfs(0,0)
        return ans