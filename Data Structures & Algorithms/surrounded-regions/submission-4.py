from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        safe_cells = set()
        for r in range(ROWS):
            if board[r][0] == "O":
                safe_cells.add((r,0))
            if board[r][COLS-1] == "O":
                safe_cells.add((r,COLS-1))
        for c in range(COLS):
            if board[0][c] == "O":
                safe_cells.add((0,c))
            if board[ROWS-1][c] == "O":
                safe_cells.add((ROWS-1, c))
        
        que = deque(safe_cells)
        dire = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        while que:
            cr, cc = que.popleft()
            if (cr, cc) in visited: continue
            visited.add((cr,cc))
            for dr, dc in dire:
                nr, nc = dr+cr, dc+cc
                if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS or 
                (nr,nc) in visited or board[nr][nc] == "X"):
                    continue
                que.append((nr, nc))
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in visited: continue
                board[row][col] = "X"
