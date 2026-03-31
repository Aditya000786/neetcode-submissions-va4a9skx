class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left = [None] * N
        right = [None] * N
        max_left, max_right = 0,0
        for i in range(N):
            max_left = max(max_left, height[i])
            left[i] = max_left
            max_right = max(max_right, height[N-1-i])
            right[N-1-i] = max_right
        
        res = 0
        for i in range(N):
            allowed_height = min(left[i], right[i]) - height[i]
            if allowed_height>0:
                res+=allowed_height
        return res

        print(left)
        print(right)
        
