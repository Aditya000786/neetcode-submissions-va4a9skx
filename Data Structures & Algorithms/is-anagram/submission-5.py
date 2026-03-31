class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a = [0]*26
        for ind in range(len(s)):
            a[ord(s[ind])-ord('a')]+=1
            a[ord(t[ind])-ord('a')]-=1

        for num in a:
            if num!=0:
                return False
        return True