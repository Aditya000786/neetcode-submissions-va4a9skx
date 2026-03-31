class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_map = {(m-1, n-1): 1}
        def dfs(position):
            if position in path_map:
                return path_map[position]
            if not (position[0]>=0 and position[0]<m and position[1]>=0 and position[1]<n):
                return 0
            if position[0] == m-1 and position[1] == n-1:
                return 1
            else:
                right = dfs((position[0]+1, position[1]))
                down = dfs((position[0], position[1]+1))
                path_map[position] = right + down
                return path_map[position]
        dfs((0,0))
        print(path_map)
        return path_map[(0,0)]