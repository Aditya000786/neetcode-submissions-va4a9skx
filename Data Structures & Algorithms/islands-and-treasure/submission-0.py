from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure_chests = []
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    treasure_chests.append((row, col))
        visited = set()
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        queue = deque(treasure_chests)
        curr_level = 0
        while queue:
            curr_level_elem = len(queue)
            curr_level += 1
            for i in range(curr_level_elem):
                row, col = queue.popleft()
                for d in dir:
                    n_row, n_col = row+d[0], col+d[1]
                    if (n_row >=0 and n_row <ROWS and n_col>=0 and n_col<COLS 
                    and (n_row, n_col) not in visited and grid[n_row][n_col] == 2147483647):
                        grid[n_row][n_col] = curr_level
                        visited.add((n_row, n_col))
                        queue.append((n_row, n_col))
