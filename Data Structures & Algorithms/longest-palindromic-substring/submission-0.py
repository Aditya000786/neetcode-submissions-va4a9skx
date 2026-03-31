class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = 1
        ans_str = s[0]
        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            mat[i][i] = 1
            
        for step in range(1, n+1):
            for i in range(0, n-step):
                if s[i] == s[i+step]:
                    sub_start = i+1
                    sub_end = i+step - 1
                    if step == 1 or mat[sub_start][sub_end]== 1:
                        mat[i][i+step] = 1
                        ans = step+1
                        ans_str = s[i:i+step+1]
                    else:
                        mat[i][i+step] = 0
                else:
                    mat[i][i+step] = 0
            # print(step)
        # print(mat)
        # return ans
        return ans_str