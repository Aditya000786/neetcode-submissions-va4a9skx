class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        ans = float('-inf')
        while left < right:
            height = min(heights[left], heights[right])
            width = right-left
            temp = height * width
            ans = max(ans, temp)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return ans