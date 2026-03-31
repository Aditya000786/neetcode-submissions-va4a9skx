class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_pali(start, end):
            nonlocal ans, ans_len 
            while start>=0 and end<len(s) and s[start] == s[end]:
                if end-start+1>ans_len:
                    ans_len = end-start+1
                    ans = s[start:end+1]
                start-=1
                end+=1

        ans = ""
        ans_len = -1
        for i in range(len(s)):
            check_pali(i, i)
            check_pali(i, i+1)
        return ans