import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mat = [["."]*n for i in range(n)]
        ans = []
        count = 0
        def place_queen(row, col, mat):
            for c in range(n):
                mat[row][c] = "X"
            for r in range(n):
                mat[r][col] = "X"

            diag = [(-1,-1), (1,1), (-1, 1), (1, -1)]
            for d in diag:
                curr_row, curr_col = row, col
                while True:
                    new_row, new_col = d[0] + curr_row, d[1] + curr_col
                    if new_row>=0 and new_row<n and new_col>=0 and new_col<n:
                        mat[new_row][new_col] = "X"
                    else:
                        break
                    curr_row, curr_col = new_row, new_col
            mat[row][col]="Q"

        def backtrack(ind, mat):
            if ind == n:
                ans.append(copy.deepcopy(mat))
                return
            for i in range(n):
                if mat[ind][i] == ".":
                    before_mat = copy.deepcopy(mat)
                    place_queen(ind, i, mat)
                    backtrack(ind+1, mat)
                    mat = before_mat
        backtrack(0, mat)
        res = []
        for a in ans:
            curr = []
            for m in a:
                s = "".join(m)
                s = s.replace("X", ".")
                curr.append(s)
            res.append(curr)
        return res
