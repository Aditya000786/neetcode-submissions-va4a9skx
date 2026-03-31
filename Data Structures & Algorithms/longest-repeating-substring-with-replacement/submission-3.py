class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left, right = 0, 0
        hash_map = {}
        max_freq = 0
        while right<len(s):
            if s[right] not in hash_map:
                hash_map[s[right]]=0
            hash_map[s[right]]+=1
            for char in hash_map.keys():
                max_freq = max(max_freq, hash_map[char])

            while right-left+1-max_freq>k:
                hash_map[s[left]]-=1
                left+=1
                for char in hash_map.keys():
                    max_freq = max(max_freq, hash_map[char])
            ans = max(ans, right-left+1)
            right+=1
        return ans