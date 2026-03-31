class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        map = {}
        low = 0
        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0) + 1
            highest = 0
            for key, count in map.items():
                if highest < count:
                    highest = count
            while i-low+1 - highest > k:
                map[s[low]] -= 1
                low+=1
            ans = max(ans, i-low+1)
        return ans