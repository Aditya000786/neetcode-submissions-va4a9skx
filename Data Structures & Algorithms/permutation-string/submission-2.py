class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l,r=0,0
        need_map = Counter(s1)
        have_map = {}
        s1_chars = set(s1)
        print(need_map)
        while r<len(s2):
            if s2[r] in s1_chars:
                print("before", need_map, r)
                if s2[r] in need_map:
                    need_map[s2[r]]-=1
                    if need_map[s2[r]]==0:
                        del need_map[s2[r]]
                else:
                    have_map[s2[r]] = 1 + have_map.get(s2[r], 0)

            if r-l+1>len(s1):
                if s2[l] in s1_chars:
                    if have_map.get(s2[l], 0)==0:
                        need_map[s2[l]] = 1 + need_map.get(s2[l], 0)
                    else:
                        have_map[s2[l]]-=1
                l+=1
            if not need_map:
                print(need_map)
                return True
            r+=1
        print("12",need_map)
        return False         