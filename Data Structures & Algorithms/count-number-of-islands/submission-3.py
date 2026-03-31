from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        level = 0
        dire = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(start):
            que = deque([start])
            while que:
                for i in range(len(que)):
                    cr, cc = que.popleft()
                    grid[cr][cc] = "0"
                    for dr, dc in dire:
                        nr, nc = cr+dr, cc+dc
                        if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS 
                            or grid[nr][nc]=="0"):
                            continue
                        que.append((nr,nc))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    level+=1
                    bfs((i,j))
        return level