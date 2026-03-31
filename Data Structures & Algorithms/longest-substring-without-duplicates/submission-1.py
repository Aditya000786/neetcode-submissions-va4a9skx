class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 
        chars = set()
        ans = 0
        while r<len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            ans = max(ans, r-l+1)
            r+=1
        return ans