class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word2), len(word1)
        dp = [[0]*(COLS+1) for i in range(ROWS+1)]
        for c in range(COLS):
            dp[-1][c] = COLS-c
        for r in range(ROWS):
            dp[r][-1] = ROWS-r
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if word1[c] == word2[r]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = 1+ min(dp[r+1][c+1], dp[r][c+1], dp[r+1][c])
        return dp[0][0]