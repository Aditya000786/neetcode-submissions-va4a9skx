class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(row, col, ind):
            if ind==len(word):
                return True
    
            if (row<0 or row>=ROWS or col<0 or col>=COLS 
                or (row, col) in visited 
                or board[row][col] != word[ind]):
                return False

            visited.add((row, col))

            ans = (dfs(row-1, col, ind+1) or dfs(row+1, col, ind+1)
            or dfs(row, col-1, ind+1) or dfs(row, col+1, ind+1))

            visited.remove((row, col))
            return ans
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j, 0): return True
        return False