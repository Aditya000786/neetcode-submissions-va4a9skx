class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        def check_pali(start, end):
            nonlocal ans
            while start>=0 and end<len(s) and s[start] == s[end]:
                if len(ans)<end-start+1:
                    ans = s[start:end+1]
                start-=1
                end+=1

        for i in range(len(s)):
            check_pali(i,i)

        for i in range(1, len(s)):
            check_pali(i-1, i)
        return ans