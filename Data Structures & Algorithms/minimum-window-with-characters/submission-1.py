class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l, r = 0, 0
        need_char = Counter(t)
        have_char = {}
        t_chars = set(t)
        ans = float('inf')
        res = ""
        while r<len(s):
            new_char = s[r]            
            if new_char in t_chars:

                if new_char in need_char:
                    need_char[new_char]-=1
                    if need_char[new_char] == 0:
                        del need_char[new_char]
                else:
                    have_char[new_char] = 1 + have_char.get(new_char, 0)
                
                while len(need_char)==0:
                    if r-l+1<ans:
                        ans = min(ans, r-l+1)
                        res = s[l:r+1]
                        # print("res", res, s[l], l, have_char, need_char)
                    left_char = s[l]
                    if left_char in t_chars:

                        if left_char in have_char:
                            have_char[left_char]-=1
                            if have_char[left_char] == 0:
                                del have_char[left_char]
                        else:
                            need_char[left_char]=1
                    l+=1
            r+=1
        return res