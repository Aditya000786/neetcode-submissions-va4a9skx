class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        for i in range(len(s)):
            map[s[i]] = max(map.get(s[i], 0), i)
        
        ans = []
        curr = 0
        while curr < len(s):
            ind = curr
            while ind != map[s[ind]]:
                for i in range(ind+1, map[s[ind]]+1):
                    if map[s[i]]>=map[s[ind]]:
                        ind = i
            ans.append(ind-curr+1)
            curr = ind+1
        return ans