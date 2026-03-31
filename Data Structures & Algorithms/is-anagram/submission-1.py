class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)>len(s):
            s,t = t,s
        c_s, c_t = dict(), dict()
        for i in s:
            c_s[i] = c_s.get(i, 0) + 1
        for i in t:
            c_t[i] = c_t.get(i, 0) + 1
        for key,_ in c_s.items():
            print(key)
            if c_s[key] != c_t.get(key, None):
                return False
        return True