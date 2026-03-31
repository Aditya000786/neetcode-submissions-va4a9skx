class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        for c in s:
            a[ord(c)-ord('a')]+=1
        for c in t:
            a[ord(c)-ord('a')]-=1
        for num in a:
            if num!=0:
                return False
        return True