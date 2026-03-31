class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_map = {}
        visited_paths = set()
        ans = 0
        def dfs(position):
            nonlocal ans
            if not (position[0]>=0 and position[0]<m and position[1]>=0 and position[1]<n):
                return
            if position in visited_paths or position[0] == m-1 and position[1] == n-1:
                ans+=1
                visited_paths.add(position)
            else:
                dfs((position[0]+1, position[1]))
                dfs((position[0], position[1]+1))
        dfs((0,0))
        return ans