class Solution:
    def isPalindrome(self, s: str) -> bool:
        org_s = ""
        for char in s:
            if ord(char)>=ord('a') and ord(char)<=ord('z'):
                org_s += char
            if ord(char)>=ord('A') and ord(char)<=ord('Z'):
                org_s += char.lower()
            if ord(char)>=ord('0') and ord(char)<=ord('9'):
                org_s += char
        if org_s == org_s[::-1]:
            return True
        return False
