class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(s):
            if len(s) == 0:
                return [[]]
            curr = []
            for i in range(0, len(s)):
                sub1 = s[0: i+1]
                if sub1 == sub1[::-1]:
                    partitions = dfs(s[i+1:])
                    for p in partitions:
                        curr.append([sub1]+p)
            return curr
        return dfs(s)