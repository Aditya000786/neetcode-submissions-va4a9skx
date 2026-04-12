class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []
        def dfs(ind):
            if ind >= len(s):
                ans.append(curr.copy())
                return
            else:
                for i in range(ind, len(s)):
                    sub = s[ind: i+1]
                    if sub == sub[::-1]:
                        curr.append(sub)
                        dfs(i+1)
                        curr.pop()
        dfs(0)
        return ans