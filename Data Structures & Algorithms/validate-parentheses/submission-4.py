class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open, close = "({[", "]})"
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if i =="]" and top!="[":
                    return False
                elif i == ")" and top!="(":
                    return False
                elif i == "}" and top!="{":
                    return False
        return True if not stack else False
