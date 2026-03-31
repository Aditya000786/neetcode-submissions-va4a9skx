class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            n = len(stack)
            while n>=k and len(set(stack[n-k:])) ==1:
                t = k
                while t>0:
                    stack.pop()
                    t-=1
                n = len(stack)
        return "".join(stack)
