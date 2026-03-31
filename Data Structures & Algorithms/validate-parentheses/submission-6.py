class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ind = 0
        op = ("(", "{", "[")
        cl = (")", "}", "]")
        while ind<len(s):
            char = s[ind]
            if char in op:
                stack.append(char)
            elif char in cl:
                if char == ")" and stack and stack[-1] == "(":
                    stack.pop()
                elif char == "}" and stack and stack[-1] == "{":
                    stack.pop()
                elif char == "]" and stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            ind+=1
        return True if len(stack)==0 else False