class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        max_left, max_right = height[left], height[right]
        ans = 0
        while left<=right:
            # print("ind", left, right, max_left, max_right, ans)
            if height[left]<height[right]:
                delta = max(0, min(max_left, max_right) - height[left])
                ans += delta
                left += 1
                max_left = max(max_left, height[left])
            else:
                delta = max(0, min(max_left, max_right) - height[right])
                ans += delta
                right -= 1
                max_right = max(max_right, height[right])
        return ans

