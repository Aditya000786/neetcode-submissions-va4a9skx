class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        mat = [[0 for c in range(COLS+1)] for r in range(ROWS+1)]
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if text1[r] == text2[c]:
                    mat[r][c] = 1 + mat[r+1][c+1]
                else:
                    mat[r][c] = max(mat[r+1][c], mat[r][c+1])
        return mat[0][0]