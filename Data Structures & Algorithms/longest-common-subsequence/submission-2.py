class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0]*(len(text2)+1)
        for r in range(len(text1)-1, -1, -1):
            curr_dp = dp.copy()
            for c in range(len(text2)-1, -1, -1):
                if text1[r] == text2[c]:
                    dp[c] = 1 + curr_dp[c+1]
                else:
                    dp[c] = max(dp[c+1], curr_dp[c])
        return dp[0]