class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []
        def dfs(ind):
            if ind==len(s):
                ans.append(curr.copy())
                return
            for i in range(ind, len(s)):
                temp = s[ind:i+1]
                if temp == temp[::-1]:
                    curr.append(temp)
                    dfs(i+1)
                    curr.pop()
        dfs(0)
        return ans