class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or t == "":
            return ""
        low, high = 0, 0
        have, need = {}, Counter(t)
        t_map= Counter(t)
        res = [-1,-1]
        reslen = float('infinity')
        while high < len(s):
            new_char = s[high]
            if new_char in have:
                have[new_char] += 1
            else:
                have[new_char] = 1

            if new_char in need:
                need[new_char]-=1
                if need[new_char] == 0:
                    del need[new_char]
                
                while len(need.keys())==0:
                    if high - low + 1<reslen:
                        res = [low, high]
                        reslen = high - low + 1

                    old_char = s[low]
                    have[old_char]-=1

                    if have[old_char] == 0:
                        del have[old_char]
                    
                    if old_char in t_map:
                        if t_map[old_char] > have.get(old_char,0):
                            need[old_char] = 1
                    
                    low+=1

            high+=1
        return s[res[0]:res[1]+1]



