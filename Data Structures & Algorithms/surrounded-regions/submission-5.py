from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        que = deque([])
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            if board[r][0] == "O":
                que.append((r,0))
            if board[r][COLS-1] == "O":
                que.append((r,COLS-1))
        
        for c in range(COLS):
            if board[0][c] == "O":
                que.append((0,c))
            if board[ROWS-1][c] == "O":
                que.append((ROWS-1,c))

        safe = set()
        dire = [(-1,0), (1,0), (0,-1), (0,1)]
        while que:
            r,c = que.popleft()
            if (r,c) in safe: continue
            safe.add((r,c))
            for dr, dc in dire:
                nr, nc = dr+r, dc+c
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS: continue
                if (nr,nc) in safe: continue
                if board[nr][nc] == "O":
                    que.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in safe:
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
        