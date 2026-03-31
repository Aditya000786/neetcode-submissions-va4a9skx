class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        start = 0 
        end = 0
        ans = 0
        while end<len(s):
            while s[end] in chars:
                chars.remove(s[start])
                start+=1
            chars.add(s[end])
            ans = max(ans, end-start+1)
            end+=1
        return ans