class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for st in strs:
            char_freq = [0]*26
            for c in st:
                ind = ord(c) - ord('a')
                char_freq[ind]+=1
            char_freq = tuple(char_freq)
            hash_map[char_freq].append(st)
        return list(hash_map.values())