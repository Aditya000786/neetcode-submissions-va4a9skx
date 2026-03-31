class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            n = len(stack)
            while n>=k and len(set(stack[n-k:])) ==1:
                stack = stack[:n-k]
                n = len(stack)
        return "".join(stack)
