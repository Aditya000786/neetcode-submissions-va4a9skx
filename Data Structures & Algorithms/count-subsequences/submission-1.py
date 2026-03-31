class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        COLS, ROWS = len(s), len(t)
        dp = [1]*(COLS+1) 
        for i in range(ROWS-1, -1, -1):
            nextDP = [0]*(COLS+1)
            for j in range(COLS-1, -1, -1):
                nextDP[j] = nextDP[j+1]
                if t[i] == s[j]:
                    nextDP[j] += dp[j+1]
            dp = nextDP
        return dp[0]