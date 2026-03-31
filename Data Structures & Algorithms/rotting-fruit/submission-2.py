from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_pieces = []
        good_pieces = set()
        ROWS, COLS = len(grid), len(grid[0])
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_pieces.append((r,c))
                if grid[r][c] == 1:
                    good_pieces.add((r,c))
        if not rotten_pieces:
            if good_pieces:
                return -1
            else:
                return 0
        queue = deque(rotten_pieces)
        level = 0
        while queue:
            cells = len(queue)
            for ind in range(cells):
                row, col = queue.popleft()
                for d in dir:
                    n_row, n_col = row + d[0], col + d[1]
                    if (n_row >=0 and n_row<ROWS and n_col>=0 and n_col<COLS and 
                    grid[n_row][n_col]==1):
                        grid[n_row][n_col] = 2
                        queue.append((n_row, n_col))
                        good_pieces.remove((n_row, n_col))
            level+=1
        return level-1 if not good_pieces else -1

