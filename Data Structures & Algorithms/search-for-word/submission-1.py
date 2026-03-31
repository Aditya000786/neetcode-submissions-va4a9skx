class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(mat_row, mat_col, ind):
            if ind==len(word):
                return True

            directions = ((-1,0), (1,0), (0,-1), (0,1), (0,0))
            for c_row, c_col in directions:
                row = mat_row + c_row
                col = mat_col + c_col
                if (row < len(board) and col<len(board[0]) and row>=0 and col>=0 and 
                word[ind] == board[row][col] and (row, col) not in visited):
                        visited.add((row, col))
                        if dfs(row, col, ind+1):
                            return True
                        visited.remove((row, col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False