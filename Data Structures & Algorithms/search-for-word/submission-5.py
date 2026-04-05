class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dire = [(-1,0), (1,0), (0,-1), (0,1)]
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, ind):
            if ind>=len(word):
                return True

            if r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c] == "#":
                return False

            if board[r][c]!=word[ind]:
                return False
            
            org_value = board[r][c]
            board[r][c] = "#"

            for dr, dc in dire:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, ind+1): return True

            board[r][c] = org_value


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False