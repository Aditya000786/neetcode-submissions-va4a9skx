class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set
        def dfs(row, col):
            if ((row<0 or row>=ROWS or col<0 or col>=COLS) or grid[row][col]=="0"):
                return
            grid[row][col]="0"
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
            return
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1":
                    dfs(i, j)
                    ans+=1
        return ans