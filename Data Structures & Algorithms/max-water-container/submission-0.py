class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low, high = 0, len(heights)-1
        ans = float('-inf')
        while low<=high:
            ans = max(ans, min(heights[low], heights[high])*(high-low))
            if heights[low]<heights[high]:
                low+=1
            else:
                high-=1
        return ans