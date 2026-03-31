class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row Check
        for i in range(9):
            hash_map = dict()
            for j in range(9):
                if board[i][j] in hash_map and board[i][j]!=".":
                    return False
                hash_map[board[i][j]] = 1
        
        # Col check
        for i in range(9):
            hash_map = dict()
            for j in range(9):
                if board[j][i] in hash_map and board[j][i]!=".":
                    return False
                hash_map[board[j][i]] = 1
        
        # 3*3 check
        for i in range(9):
            row_start = i//3 * 3
            col_start = i%3 * 3
            hash_map = dict()
            for row in range(row_start, row_start+3):
                for col in range(col_start, col_start+3):
                    if board[row][col] in hash_map and board[row][col]!=".":
                        return False
                    hash_map[board[row][col]] = 1


        return True