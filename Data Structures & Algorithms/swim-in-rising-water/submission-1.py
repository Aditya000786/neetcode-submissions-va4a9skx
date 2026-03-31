import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t = 0
        heap = [(grid[0][0], (0,0))]
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            n_time, position = heapq.heappop(heap)
            t = max(t, n_time)
            if position[0] == ROWS-1 and position[1] == COLS-1:
                return t
            if position not in visited:
                visited.add(position)
                for dr in directions:
                    n_row, n_col = dr[0] + position[0], dr[1] + position[1]
                    if (n_row >= 0 and n_row < ROWS and n_col >= 0 and n_col < COLS
                    and (n_row, n_col) not in visited):
                        heapq.heappush(heap, (grid[n_row][n_col], (n_row, n_col)))