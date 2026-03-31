class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for s in strs:
            final_str += str(len(s)) + "_" + s
        return final_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i;
            leng = ""
            while s[j]!="_":
                leng+=s[j]
                j+=1
            i=j+1
            leng = int(leng)
            ans.append(s[i:i+leng])
            i+=leng
        return ans