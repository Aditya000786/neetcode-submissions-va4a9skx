class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        saved_cells = set()
        def dfs(row, col):
            if (row<0 or row==ROWS or col<0 or col==COLS or 
            (row, col) in saved_cells or board[row][col]=="X"):
                return
            saved_cells.add((row, col))

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in saved_cells:
                    board[r][c] = "X"
    