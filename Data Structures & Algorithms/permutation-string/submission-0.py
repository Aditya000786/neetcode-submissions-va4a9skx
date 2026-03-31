

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_map = Counter(s1)
        s2_map = Counter(s2[:len(s1)])
        have, need = s2_map, {}
        for s1_char, s1_count in s1_map.items():
            s2_count = s2_map.get(s1_char, 0)
            if s2_count<s1_count:
                need[s1_char] = s1_count-s2_count
        if len(need)==0:
            return True
        for right in range(len(s1), len(s2)):
            low = right-len(s1)
            old_char = s2[low]
            have[old_char]-=1
            if have[old_char] == 0:
                del have[old_char]
            
            if old_char in s1_map and have.get(old_char,0)<s1_map[old_char]:
                if old_char in need:
                    need[old_char]+=1
                else:
                    need[old_char] = 1

            low+=1

            new_char = s2[right]
            if new_char in have:
                have[new_char] +=1
            else:
                have[new_char] = 1
            
            if new_char in need:
                need[new_char]-=1
                if need[new_char]==0:
                    del need[new_char]
            
            if len(need)==0:
                return True
        return False


# Convert s1 to hash_map
# abc -> {a:1, b:1, c:1}
# Sliding window of length of hashmap
# Convert that into hashmap and then compare 2 hashmap

# O(n.m)

# have = {"l":1,"e":1,"c":1}
# need = {"a":1, "b":1, "c": 1}

# Shift window by 1, check if needed element in there:
#     if its there, reduce need count by 1 and increase have
# Shift lower side reduce from having of lower elemen