class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        ans = 0
        stack = [[heights[0], 1]]
        for i in range(1, len(heights)):
            print(stack)
            new = heights[i]
            if new <= stack[-1][0]:
                total_count = 0
                while stack and new <= stack[-1][0]:
                    elem, elem_count = stack.pop()
                    total_count += elem_count
                    ans = max(ans, elem*total_count)
                stack.append([new, total_count+1])
            elif new>stack[-1][0]:
                stack.append([new, 1])
        while stack:
            top_elem, top_count = stack.pop()
            ans = max(ans, top_elem*top_count)
            if stack and top_elem >= stack[-1][0]:
                stack[-1][1]+= top_count
        return ans