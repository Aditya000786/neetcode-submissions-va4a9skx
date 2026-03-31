class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                ans.append(0)
            elif temperatures[i] < stack[-1][0]:
                ans.append(1)
            else:
                while stack and temperatures[i]>=stack[-1][0]:
                    stack.pop()
                if not stack:
                    ans.append(0)
                else:
                    ans.append(stack[-1][1]-i)
            stack.append((temperatures[i], i))
        return ans[::-1]