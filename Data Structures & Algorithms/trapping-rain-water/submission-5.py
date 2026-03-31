class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        left, right = 0, len(height)-1
        ans = 0
        while left<right:
            if maxRight < maxLeft:
                right-=1
                maxRight = max(maxRight, height[right])
                ans+=maxRight-height[right]
            else:
                left+=1
                maxLeft = max(maxLeft, height[left])
                ans+=maxLeft-height[left]
        return ans