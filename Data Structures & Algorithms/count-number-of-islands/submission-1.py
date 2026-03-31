class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        ans = 0
        visited = set()
        def dfs(row, col):
            grid[row][col]="0"
            visited.add((row, col))
            dir = ((-1,0), (1,0), (0,-1), (0, 1))
            for d in dir:
                new_row, new_col = d[0] + row, d[1] + col
                if (new_row>=0 and new_row<ROW and new_col>=0 and new_col < COL 
                    and grid[new_row][new_col] == "1"):
                    dfs(new_row, new_col)
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col]=="1":
                    ans+=1
                    dfs(row, col)
        return ans