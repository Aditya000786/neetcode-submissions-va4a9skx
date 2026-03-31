class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        mat = [[ None for col in range(N)] for row in range(N)]
        for i in range(N):
            mat[i][i]=1
        res = s[0]
        def sub(start, end):
            nonlocal res
            if start>end:
                return 0
            if not mat[start][end]:
                if s[start] == s[end] and sub(start+1, end-1)!=-1:
                    mat[start][end] = sub(start+1, end-1)+2
                    if len(res)<end-start+1:
                        res = s[start:end+1]
                else:
                    mat[start][end] = -1
                    sub(start, end-1)
                    sub(start+1, end)
            return mat[start][end]
        sub(0,N-1)
        print(mat)
        return res