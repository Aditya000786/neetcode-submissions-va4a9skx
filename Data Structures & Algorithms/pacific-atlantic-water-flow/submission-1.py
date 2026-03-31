from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def traverse_land(sea, que):
            while que:
                for i in range(len(que)):
                    cr, cc = que.popleft()
                    sea.add((cr, cc))
                    for dr, dc in dir:
                        nr, nc = cr+dr, cc+dc
                        if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS or
                            (nr, nc) in sea or
                            heights[nr][nc]<heights[cr][cc]):
                            continue
                        que.append((nr, nc))

        atlantic, pacific = set(), set()
        dir = [(-1,0), (1, 0), (0,-1), (0,1)]
        ROWS, COLS = len(heights), len(heights[0])
        start=([(0, col) for col in range(0, COLS)] + 
            [(row,0) for row in range(1, ROWS)])
        que = deque(start)
        traverse_land(pacific, que)

        start=(
            [(ROWS-1, col) for col in range(0, COLS)] + 
            [(row,COLS-1) for row in range(0, ROWS-1)]
            )
        que = deque(start)
        traverse_land(atlantic, que)
        ans = list()
        for spot in atlantic:
            if spot in pacific:
                ans.append(list(spot))
        return ans
        