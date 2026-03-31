class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_chars = set(["(", "{", "["])
        closed_chars = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in open_chars:
                stack.append(char)
            if char in closed_chars:
                if len(stack)==0 or closed_chars[char]!=stack.pop():
                    return False
        if len(stack)!=0:
            return False
        return True