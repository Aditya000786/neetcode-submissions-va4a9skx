class Solution:
    def trap(self, height: List[int]) -> int:
        ind = 0
        stack = [ind]  
        ind+=1    
        ans = 0
        while ind < len(height):
            while stack and height[stack[-1]]<height[ind]:
                pop_ind = stack.pop()
                if not stack:
                    break

                ans += (min(height[stack[-1]], height[ind]) - height[pop_ind])*(ind-stack[-1]-1)
            stack.append(ind)
            ind+=1
        return ans