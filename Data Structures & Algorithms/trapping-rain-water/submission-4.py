class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        left, right = 0, len(height)-1
        ans = 0
        while left<=right:
            if maxRight < maxLeft:
                ans+=max(0, maxRight-height[right])
                maxRight = max(maxRight, height[right])
                right-=1
            else:
                ans+=max(0, maxLeft-height[left])
                maxLeft = max(maxLeft, height[left])
                left+=1
        return ans