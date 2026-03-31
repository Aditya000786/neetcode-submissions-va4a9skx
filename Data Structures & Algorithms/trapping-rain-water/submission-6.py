class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * (n)
        suffix = [0] * (n)
        for i in range(n):
            if 0<i<n:
                prefix[i] = max(prefix[i-1], height[i-1])
            j = n-1-i
            if j<n-1:
                suffix[j] = max(suffix[j+1], height[j+1])
        
        ans = 0
        for i in range(n):
            curr_height = min(prefix[i], suffix[i])
            delta = max(0, curr_height-height[i])
            ans += delta
        return ans