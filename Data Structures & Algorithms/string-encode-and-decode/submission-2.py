class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            c = str(len(s))
            ans+=c+"#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        print("s",s)
        ans = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            str_length = int(s[i:j])

            str_end_index = j + str_length

            curr_word = s[j + 1: str_end_index+1]
            ans.append(curr_word)
            i = str_end_index + 1
        return ans
