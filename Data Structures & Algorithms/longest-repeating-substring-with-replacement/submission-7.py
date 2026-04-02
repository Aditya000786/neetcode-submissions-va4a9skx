class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                # print(s[start:end])
                sub = s[start:end]
                sub_len = len(sub)
                c = Counter(sub)
                max_occur = 0
                for key, value in c.items():
                    if value>max_occur:
                        max_occur = max(max_occur, value)
                if sub_len - max_occur<=k:
                    ans = max(ans, sub_len)
                else:
                    break
        return ans