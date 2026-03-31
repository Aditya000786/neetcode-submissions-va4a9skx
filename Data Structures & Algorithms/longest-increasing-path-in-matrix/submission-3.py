from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[None]*COLS for i in range(ROWS)]
        dire = [(-1,0), (1,0), (0,-1), (0,1)]

        @lru_cache(None)
        def dfs(row, col):
            ans = 0
            for dr, dc in dire:
                nr, nc = row+dr, col + dc
                if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS
                or matrix[nr][nc]<=matrix[row][col]): 
                    continue
                ans = max(ans, dfs(nr, nc)+1)
            return ans
                
        ans = 0
        for row in range(ROWS):
            for col in range(COLS):
                ans = max(ans, dfs(row, col))
        return ans+1