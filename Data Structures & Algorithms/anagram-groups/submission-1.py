class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for str in strs:
            num = [0]*26
            for s in str:
                num[ord(s)-ord('a')]+=1
            hash_map.setdefault(tuple(num), []).append(str)
        return [val for val in hash_map.values()]