class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        char = set()
        ans = 0
        while r < len(s):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            ans = max(ans, len(char))
            r+=1
        return ans