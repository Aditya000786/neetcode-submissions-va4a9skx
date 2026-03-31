from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()
        ROWS, COLS = len(board), len(board[0])
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        for c in range(COLS):
            if board[0][c] == "O":
                safe.add((0, c))
            if board[ROWS-1][c] == "O":
                safe.add((ROWS-1, c))
            
        for r in range(ROWS):
            if board[r][0] == "O":
                safe.add((r, 0))

            if board[r][COLS-1] == "O":
                safe.add((r, COLS-1))
        print("safe", safe)
        que = deque(safe)
        while que:
            for i in range(len(que)):
                cr, cc = que.popleft()
                for dr, dc in dir:
                    nr, nc = dr+cr, dc + cc
                    if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS 
                        or (nr, nc) in safe or board[nr][nc]=="X"):
                        continue
                    safe.add((nr, nc))
                    que.append((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in safe:
                    board[r][c] = "X"
