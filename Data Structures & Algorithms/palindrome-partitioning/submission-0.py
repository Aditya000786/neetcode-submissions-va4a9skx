from typing import List
class Solution:
    def is_pali(self, i, j, s):
        if i==j:
            return True
        while i<=j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(start):
            if start>=len(s):
                res.append(part.copy())
                return
            for step in range(0, len(s)):
                if start+step>=len(s):
                    break
                part.append(s[start:start+step+1])
                if self.is_pali(start, start+step, s):
                    dfs(start+step+1)
                part.pop()
        dfs(0)
        return res