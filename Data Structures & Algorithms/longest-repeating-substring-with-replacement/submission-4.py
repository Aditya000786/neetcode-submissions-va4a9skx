class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left, right = 0, 0
        hash_map = {}
        max_freq = 0
        while right<len(s):
            hash_map[s[right]] = 1 + hash_map.get(s[right], 0)
            max_freq = max(max_freq, hash_map[s[right]])
            
            while right-left+1-max_freq>k:
                hash_map[s[left]]-=1
                left+=1
            ans = max(ans, right-left+1)
            right+=1
        return ans