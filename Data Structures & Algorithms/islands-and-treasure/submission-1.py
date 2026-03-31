from collections import deque
from functools import lru_cache
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0]) 
        @lru_cache(None)
        def dp(row, col):
            print("dim",row, col)
            if (row<0 or row>=ROWS or col<0 or col>=COLS
                or grid[row][col]==-1):
                return float('inf')
            if grid[row][col] == 0: return 1

            grid[row][col] = min(
                dp(row-1, col),
                dp(row+1, col),
                dp(row, col-1),
                dp(row, col+1)
            )
            return grid[row][col]
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         grid[i][j] = dp(i, j)
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        def bfs(row, col):
            que = deque([(row, col)])
            level = 0
            visited = set()
            found = False
            while que and not found:
                for i in range(len(que)):
                    cr, cc = que.popleft()
                    if grid[cr][cc]==0:
                        grid[row][col] = level
                        found = True
                        break
                    visited.add((cr, cc))
                    for dr, dc in dir:
                        nr,nc = cr+dr, cc+dc
                        if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS 
                        or grid[nr][nc]==-1 or (nr, nc) in visited):
                            continue
                        que.append((nr, nc))
                level+=1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]!=-1 and grid[i][j]!=0:
                    bfs(i,j)

