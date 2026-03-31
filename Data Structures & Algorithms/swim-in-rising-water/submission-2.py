import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        heap = [[grid[0][0], (0,0)]]
        heapq.heapify(heap)
        visited = set()
        ans = 0
        dire = [(-1,0), (1,0), (0,-1), (0,1)]
        while heap:
            curr_time, (row, col) = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            ans = max(ans, curr_time)
            if row == ROWS-1 and col == COLS-1:
                break
            visited.add((row, col))
            for dr, dc in dire:
                nr, nc = row + dr, col + dc
                if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS
                or (nr, nc) in visited):
                    continue
                heapq.heappush(heap, (grid[nr][nc], (nr, nc)))

        return ans