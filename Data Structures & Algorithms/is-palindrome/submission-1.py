class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start<=end<len(s):
            if not s[start].isalnum():
                start+=1
                continue
            if not s[end].isalnum():
                end-=1
                continue
            if s[start].lower()==s[end].lower():
                start,end = start+1, end-1
            else:
                print(start, end)
                print(s[start], s[end])
                return False
        return True