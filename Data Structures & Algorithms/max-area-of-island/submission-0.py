class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area = 0
        ans = 0
        def dfs(row, col):
            nonlocal area
            area+=1
            visited.add((row, col))
            direc = [(-1,0), (1,0), (0,-1), (0,1)]
            for d in direc:
                new_row, new_col = d[0] + row, d[1] + col
                if (new_row>=0 and new_row<ROWS and new_col>=0 and new_col<COLS 
                    and (new_row, new_col) not in visited and grid[new_row][new_col] == 1):
                    dfs(new_row, new_col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    visited = set()
                    area = 0
                    dfs(row, col)
                    ans = max(ans, area)
        return ans