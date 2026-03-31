class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        mat = [[ None for col in range(N)] for row in range(N)]
        for i in range(N):
            mat[i][i]=1
        res = len(s)
        def sub(start, end):
            nonlocal res
            if start>end:
                return 0
            if not mat[start][end]:
                if s[start] == s[end] and sub(start+1, end-1)!=-1:
                    mat[start][end] = sub(start+1, end-1)+2
                    res+=1
                else:
                    mat[start][end] = -1
                    sub(start, end-1)
                    sub(start+1, end)
            return mat[start][end]
        for i in range(N):
            for j in range(i+1,N):
                sub(i, j)
        # print(mat)
        return res