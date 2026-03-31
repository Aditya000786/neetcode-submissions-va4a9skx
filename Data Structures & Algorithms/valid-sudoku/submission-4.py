class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row
        for r in range(9):
            elem = set()
            for c in range(9):
                if board[r][c]!=".":
                    if board[r][c] in elem:
                        return False
                    elem.add(board[r][c])

        # Col
        for c in range(9):
            elem = set()
            for r in range(9):
                if board[r][c]!=".":
                    if board[r][c] in elem:
                        return False
                    elem.add(board[r][c])

        start_row = 0
        while start_row<9:
            start_col = 0
            while start_col<9:
                elem = set()
                for c in range(start_col, 3+start_col):
                    for r in range(start_row,3+start_row):
                        if board[r][c]!=".":
                            if board[r][c] in elem:
                                return False
                            elem.add(board[r][c])
                start_col+=3
            start_row+=3
        return True