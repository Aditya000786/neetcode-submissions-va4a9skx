class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        ans = 0
        chars = Counter()
        while right<len(s):
            while s[right] in chars and chars[s[right]]>0:
                chars[s[left]] = chars[s[left]]-1
                left+=1
            chars[s[right]] = chars.get(s[right], 0)+1
            right+=1
            ans = max(right-left,ans)
        return ans