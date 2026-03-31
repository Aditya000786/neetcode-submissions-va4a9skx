class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for curr in strs:
            new_key = [0]*26
            for char in curr:
                new_key[ord(char)-ord('a')]+=1
            groups.setdefault(str(new_key), []).append(curr)
        res = []
        for value in groups.values():
            res.append(value)
        return res