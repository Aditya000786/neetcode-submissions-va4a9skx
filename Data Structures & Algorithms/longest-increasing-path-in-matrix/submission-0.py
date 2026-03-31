class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 1
        def dfs(row, col):
            nonlocal res
            if row<0 or row>=ROWS or col<0 or col>=COLS:
                return 0
            if (row, col) in cache:
                return cache[(row,col)]
            dir = [(-1,0), (1,0), (0,-1), (0,1)]
            ans = 1
            for dx, dy in dir:
                nr, nc = row+dx, col+dy
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS:
                    continue
                if matrix[nr][nc]>matrix[row][col]:
                    ans = max(ans, 1+dfs(nr, nc))
            cache[(row,col)] = ans
            res = max(res, ans)
            return ans
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j)
        return res