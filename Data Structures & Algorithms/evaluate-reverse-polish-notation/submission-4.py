from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        curr = 0
        while curr<len(tokens):
            while curr<len(tokens) and tokens[curr] not in ("+", "*", "-", "/"):
                stack.append(tokens[curr])
                curr+=1

            if len(stack)==1:
                break

            num2 = stack.pop()
            num1 = stack.pop()
            oper = tokens[curr]
            res = self.perform_op(int(num1), int(num2), oper)
            curr+=1
            stack.append(res)
        return int(stack[0])
    
    def perform_op(self, num1, num2, oper):
            if oper == "+":
                return num1 + num2
            if oper == "-":
                return num1 - num2
            if oper == "*":
                return num1 * num2
            if oper == "/":
                return int(num1 / num2)
