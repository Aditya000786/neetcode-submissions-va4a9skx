class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, columns = len(text1)+1, len(text2)+1
        dp = [[None]*(columns) for _ in range(rows)]
        # print("dp", dp)
        for i in range(rows):
            dp[i][len(text2)] = 0
        for i in range(columns):
            dp[len(text1)][i] = 0
        
        for curr_row in range(rows-2, -1, -1):
            for curr_col in range(columns - 2, -1, -1):
                if text1[curr_row] == text2[curr_col]:
                    dp[curr_row][curr_col] = 1 + dp[curr_row+1][curr_col+1]
                else:
                    dp[curr_row][curr_col] = max(dp[curr_row][curr_col+1], dp[curr_row+1][curr_col])
        return dp[0][0]