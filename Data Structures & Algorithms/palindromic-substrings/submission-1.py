class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        def check_pali(start, end):
            nonlocal ans 
            while start>=0 and end<len(s) and s[start] == s[end]:
                ans+=1
                start-=1
                end+=1

        for i in range(len(s)):
            check_pali(i, i)
            check_pali(i, i+1)
        return ans