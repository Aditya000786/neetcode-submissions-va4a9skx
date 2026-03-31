from collections import deque
import copy

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        treasure_lands = []
        dire = [(-1,0), (1,0), (0,-1), (0,1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasure_lands.append((r,c))
        que = deque(treasure_lands)
        level = 0
        while que:
            level+=1
            for i in range(len(que)):
                cr, cc = que.popleft()
                for dr, dc in dire:
                    nr, nc = dr+cr, dc+cc
                    if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS or 
                        grid[nr][nc]==-1 or grid[nr][nc]==0):
                        continue
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = level
                        que.append((nr, nc))
