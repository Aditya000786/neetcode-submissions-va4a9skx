class Solution:
    def __init__(self):
        self.hash_map = {}
    def climbStairs(self, n: int) -> int:
        if n in self.hash_map:
            return self.hash_map[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            self.hash_map[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.hash_map[n]
