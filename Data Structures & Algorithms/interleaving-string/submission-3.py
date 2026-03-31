class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        def backtrack(ind1, ind2):
            if (ind1, ind2) in cache:
                return cache[(ind1,ind2)]
            if ind1+ind2 == len(s3):
                return True
            else:
                if ind1<len(s1) and s1[ind1] == s3[ind1+ind2] and backtrack(ind1+1, ind2):
                    cache[(ind1, ind2)] = True
                elif ind2<len(s2) and s2[ind2] == s3[ind1+ind2] and backtrack(ind1, ind2+1):
                    cache[(ind1, ind2)] = True
                else:
                    cache[(ind1, ind2)] = False
            return cache[(ind1, ind2)]
        if len(s1)+len(s2)!= len(s3):
            return False
        ans = backtrack(0,0)
        return ans