class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ind = 0
        while ind<len(tokens):
            curr = tokens[ind]
            if curr not in ("+", "-", "*", "/"):
                stack.append(curr)
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if curr == "+":
                    ans = op1+op2
                elif curr == "-":
                    ans = op1-op2
                elif curr == "*":
                    ans = op1*op2
                elif curr == "/":
                    ans = op1/op2 
                stack.append(ans)
            ind+=1
        return int(stack[-1])