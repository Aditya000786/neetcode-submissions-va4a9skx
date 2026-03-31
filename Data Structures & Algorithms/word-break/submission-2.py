class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {word: True for word in wordDict}
        cache[""] = True
        def sub(s):
            if s in cache:
                return cache[s]
            for word in wordDict:
                t = len(word)
                if s[0:t] == word:
                    res = sub(s[t:])
                    if res:
                        cache[s] = True
                        return True
            cache[s] = False
            return False
        return sub(s)