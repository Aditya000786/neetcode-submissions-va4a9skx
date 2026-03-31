from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        start = []
        ans = 0
        is_rotten = False
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    is_rotten = True
                    start.append((r,c))
        que = deque(start)
        while que:
            ans+=1
            for i in range(len(que)):
                cr, cc = que.popleft()
                for dr, dc in dir:
                    nr, nc = cr + dr, cc + dc
                    if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS
                        or grid[nr][nc]==0 or grid[nr][nc]==2):
                        continue
                    grid[nr][nc]=2
                    que.append((nr, nc))
        
        is_fresh = False
        for r in range(ROWS):
            if is_fresh: break
            for c in range(COLS):
                if grid[r][c] == 1:
                    is_fresh = True
                    break

        if is_fresh: return -1
        if not is_rotten : return 0
        return ans-1