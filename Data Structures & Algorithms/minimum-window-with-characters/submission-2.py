class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_hash = Counter(t)
        need = Counter(t)
        have = {}
        l, r = 0,0
        ans = ""
        ans_len = float('inf')
        while r<len(s):
            new_char = s[r]
            have[new_char] = have.get(new_char, 0) + 1
            if new_char in need:
                need[new_char] -= 1
                if need[new_char] == 0:
                    del need[new_char]
            while len(need)==0:
                if ans_len>r-l+1:
                    ans = s[l:r+1]
                    ans_len = r-l+1

                left_most_char = s[l]
                if have[left_most_char]==t_hash.get(left_most_char,0):
                    need[left_most_char] = need.get(left_most_char, 0) +1

                l+=1
                have[left_most_char]-=1
                if have[left_most_char] == 0:
                    del have[left_most_char] 
            r+=1
        return ans