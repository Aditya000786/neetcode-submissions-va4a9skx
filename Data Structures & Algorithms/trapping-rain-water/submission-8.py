class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        max_left, max_right = height[left], height[right]
        ans = 0
        while left<right:
            if height[left]<height[right]:
                left += 1
                max_left = max(max_left, height[left])
                ans += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                ans += max_right - height[right]
        return ans

