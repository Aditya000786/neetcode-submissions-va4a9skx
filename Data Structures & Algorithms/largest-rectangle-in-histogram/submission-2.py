class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        N = len(heights)
        for ind in range(N):
            temp = ind
            while stack and stack[-1][0]>heights[ind]:
                num, num_ind = stack.pop()
                ans = max(ans, num*(ind-num_ind))
                temp = num_ind
            stack.append((heights[ind], temp))
        while stack:
            num, num_ind = stack.pop()
            ans = max(ans, num*(N-num_ind))         
        return ans