class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            key = [0]*26
            for char in s:
                key[ord(char) - ord('a')]+=1
            key = str(key)
            hash_map[key].append(s)
        return list(hash_map.values())
