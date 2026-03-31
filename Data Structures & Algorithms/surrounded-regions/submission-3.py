class Solution:
    def solve(self, board: List[List[str]]) -> None:
        save_cells = set()
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            if board[r][0] == "O":
                save_cells.add((r,0))
            if board[r][COLS-1] == "O":
                save_cells.add((r,COLS-1))
        
        for c in range(COLS):
            if board[0][c] == "O":
                save_cells.add((0,c))
            if board[ROWS-1][c] == "O":
                save_cells.add((ROWS-1,c))

        que = deque(save_cells)
        dire = [(-1,0), (0,-1), (0,1), (1,0)]
        while que:
            for i in range(len(que)):
                cr, cc = que.popleft()
                for dr, dc in dire:
                    nr, nc = dr+cr, dc+cc
                    if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS or board[nr][nc]=="X"
                    or (nr,nc) in save_cells):
                        continue
                    save_cells.add((nr,nc))
                    que.append((nr,nc))
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in save_cells:
                    board[i][j] = "X"





