class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        COLS, ROWS = len(s), len(t)
        dp = [[0 for col in range(COLS+1)] for row in range(ROWS+1)]
        dp[-1] = [1]*(COLS+1)
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                dp[i][j] = dp[i][j+1]
                if t[i] == s[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]