from collections import defaultdict
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore_islands(row:int, col:int, count: int):
            visited[(row, col)] = True
            island_count[(row, col)] = count if grid[row][col]=='1' else -1 
            neighbours = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
            for neigh in neighbours:
                if 0<=neigh[0]<len(grid) and 0<=neigh[1]<len(grid[0]):
                    if not visited[neigh] and grid[neigh[0]][neigh[1]]=='1':
                        explore_islands(neigh[0], neigh[1], count)
                    
        visited = defaultdict(bool)
        island_count = defaultdict(int)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='0':
                    visited[(row, col)] = True
                    continue
                if not visited[(row, col)]:
                    count+=1
                explore_islands(row, col, count)
        return count
                